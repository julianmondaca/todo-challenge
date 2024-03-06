from datetime import datetime
from backend.models import Note, Status

class NoteRepository:
    def __init__(self):
        pass

    def create_note(self, content, status_id):
        try:
            status = Status.objects.get(id=status_id)
            note = Note.objects.create(
                content=content,
                date_created=datetime.now(),
                status=status
            )
            return note
        except Exception as e:
            print("Ocurrio un error al intentar crear una nueva nota")
            raise e

    def update_note(self, note_id, content, status_id):
        try:
            Note.objects.filter(id = note_id, date_deleted__isnull = True).update(
                content = content,
                date_updated = datetime.now(),
                status_id = status_id
            )
        except Exception as e:
            print("Ocurrio un error al intentar actualizar una nota")
            raise e
        
    def delete_note(self, note_id):
        try:
            Note.objects.filter(id = note_id, date_deleted__isnull = True).update(
                date_deleted = datetime.now()
            )
        except Exception as e:
            print("Ocurrio un error al intentar borrar una nota")
            raise e