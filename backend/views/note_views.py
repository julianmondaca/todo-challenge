import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.http import require_http_methods
from backend.services.note_service import NoteService

@csrf_exempt
@require_http_methods(["POST", "PUT"])
@permission_classes([IsAuthenticated])
def create_or_update_note(request):
        data = json.loads(request.body.decode('utf-8'))
        content = data.get('content')
        status_id = data.get('status_id')
        note_id = data.get('note_id')
        
        if not content or not status_id:
            return JsonResponse({'error': 'Se requiere contenido y el id de estado para crear o actualizar una nota.'}, status=400)

        note_service = NoteService()

        if request.method == "PUT":
            if not note_id:
                return JsonResponse({'error': 'Se requiere un id de nota para actualizar una nota.'}, status=400)
            try:
                note_service.update_note(note_id, content, status_id)
                return JsonResponse({"Message":"Se actualizo la nota con exito"}, status=200)
            except Exception as e:
                 return JsonResponse({'error': 'Ocurrio un error al intentar actualizar una nota.'}, status=400)

        try:
             note_service.create_note(content, status_id)
             return JsonResponse({"Message":"Se creo la nota con exito"}, status=200)
        except Exception as e:
             return JsonResponse({'error': 'Ocurrio un error al intentar crear una nota.'}, status=400)
        
            
@csrf_exempt
@require_http_methods(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_note(request, note_id):
     if not note_id:
         return JsonResponse({'error': 'Se requiere un id de nota para eliminar una nota.'}, status=400)
     note_service = NoteService()
     try:
         note_service.delete_note(note_id)
         return JsonResponse({"Message":"Se eliminó la nota con exito"}, status=200)
     except Exception as e:
         return JsonResponse({'error': 'Ocurrio un error al intentar eliminar una nota.'}, status=400)