import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
import django
django.setup()


import pytest
from unittest.mock import MagicMock, patch
from backend.services.note_service import NoteService
from backend.repository.note_repository import NoteRepository
from backend.models import Note

@pytest.fixture
def mock_note_repository():
    return Note(id = 1, content = "content", status_id = 1)

@pytest.fixture
def error_fixture():
    return ValueError("Error fixture")

def test_create_note_success(mock_note_repository):
    content = "test content"
    status_id = 1
    with patch.object(NoteRepository, 'create_note', return_value=mock_note_repository) as mock_note:

        note_service = NoteService()
        result = note_service.create_note(content, status_id)

        assert result.id == 1
        assert mock_note.call_count == 1

def test_create_note_fail(error_fixture):
    content = "test content"
    status_id = 1
    with patch.object(NoteRepository, 'create_note', side_effect=error_fixture) as mock_note:

        note_service = NoteService()
        try:
            note_service.create_note(content, status_id)
            assert False
        except Exception:
            assert True


        assert mock_note.call_count == 1

def test_update_note_success():
    content = "test content"
    status_id = 1
    note_id = 1
    with patch.object(NoteRepository, 'update_note', side_effect=None) as mock_note_updated:

        note_service = NoteService()
        note_service.update_note(note_id, content, status_id)

        assert mock_note_updated.call_count == 1

def test_update_note_fail(error_fixture):
    content = "test content"
    status_id = 1
    note_id = 1
    with patch.object(NoteRepository, 'update_note', side_effect=error_fixture) as mock_note_updated:

        note_service = NoteService()
        try:
            note_service.update_note(note_id, content, status_id)
            assert False
        except Exception:
            assert True

        assert mock_note_updated.call_count == 1

def test_delete_note_success():
    note_id = 1
    with patch.object(NoteRepository, 'delete_note', side_effect=None) as mock_note_deleted:

        note_service = NoteService()
        note_service.delete_note(note_id)

        assert mock_note_deleted.call_count == 1


def test_delete_note_fail(error_fixture):
    note_id = 1
    with patch.object(NoteRepository, 'delete_note', side_effect=error_fixture) as mock_note_deleted:

        note_service = NoteService()
        try:
            note_service.delete_note(note_id)
            assert False
        except Exception:
            assert True

        assert mock_note_deleted.call_count == 1