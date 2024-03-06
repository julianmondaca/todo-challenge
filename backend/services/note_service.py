from backend.repository.note_repository import NoteRepository

class NoteService:
    def __init__(self):
        pass

    def create_note(self, content, status_id):
        try:
            note_repository = NoteRepository()
            note = note_repository.create_note(content, status_id)
            return note
        except Exception as e:
            print("ocurrio un error al intentar crear una nueva nota. Error: ", e)
            raise e
        
    def update_note(self, note_id, content, status_id):
        try:
            note_repository = NoteRepository()
            note = note_repository.update_note(note_id, content, status_id)
            return note
        except Exception as e:
            print("ocurrio un error al intentar actualizar una nota. Error: ", e)
            raise e
        
    def delete_note(self, note_id):
        try:
            note_repository = NoteRepository()
            note = note_repository.delete_note(note_id)
            return note
        except Exception as e:
            print("ocurrio un error al intentar borrar una nota. Error: ", e)
            raise e