import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
import django
django.setup()

import pytest
from datetime import datetime
from unittest.mock import patch
from unittest.mock import Mock
from backend.repository.note_repository import NoteRepository


@pytest.fixture
def error_fixture():
    return ValueError("Error fixture")

def test_create_note_success():
    mocked_status = Mock(id=1)
    mocked_note = Mock(content="test note", date_created=datetime.now(), status=mocked_status)
    with patch('backend.models.Status.objects.get', return_value=mocked_status) as mock_get_status, \
         patch('backend.models.Note.objects.create', return_value=mocked_note) as mock_create_note:

        content = "test note"
        status_id = 1
        note_repository = NoteRepository()
    
        note = note_repository.create_note(content, status_id)

        assert note.content == content
        assert isinstance(note.date_created, datetime)
        assert note.status.id == status_id

        assert mock_get_status.called
        assert mock_create_note.called

def test_create_note_fail(error_fixture):
    mocked_status = error_fixture
    mocked_note = Mock(content="test note", date_created=datetime.now(), status=mocked_status)
    with patch('backend.models.Status.objects.get', side_effect=error_fixture) as mock_get_status, \
         patch('backend.models.Note.objects.create', return_value=mocked_note) as mock_create_note:

        content = "test note"
        status_id = 1
        note_repository = NoteRepository()
        try:
            note_repository.create_note(content, status_id)
            assert False
        except ValueError:
            assert True

        assert mock_get_status.called
        assert mock_create_note.call_count == 0

def test_update_note_success():
    mocked_status = Mock(id=1)
    mocked_note = Mock(content="test note", date_created=datetime.now(), status=mocked_status)
    with patch('backend.models.Note.objects.filter', return_value=mocked_note) as mock_update_note:

        content = "test note"
        status_id = 1
        note_id = 1
        note_repository = NoteRepository()
    
        note_repository.update_note(note_id, content, status_id)

        mock_update_note.return_value.update = 1

        assert mock_update_note.called

def test_update_note_fail(error_fixture):
    with patch('backend.models.Note.objects.filter', side_effect=error_fixture) as mock_update_note:

        content = "test note"
        status_id = 1
        note_id = 1
        note_repository = NoteRepository()
        try:
            note_repository.update_note(note_id, content, status_id)
            assert False
        except ValueError:
            assert True

        assert mock_update_note.called

def test_delete_note_success():
    mocked_status = Mock(id=1)
    mocked_note = Mock(content="test note", date_created=datetime.now(), status=mocked_status)
    with patch('backend.models.Note.objects.filter', return_value=mocked_note) as mock_deleted_note:

        note_id = 1
        note_repository = NoteRepository()
    
        note_repository.delete_note(note_id)

        mock_deleted_note.return_value.delete = 1

        assert mock_deleted_note.called

def test_delete_note_fail(error_fixture):
    with patch('backend.models.Note.objects.filter', side_effect=error_fixture) as mock_deleted_note:

        note_id = 1
        note_repository = NoteRepository()
    
        try:
            note_repository.delete_note(note_id)
            assert False
        except ValueError:
            assert True

        assert mock_deleted_note.called