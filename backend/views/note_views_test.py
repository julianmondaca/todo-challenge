import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
import django
django.setup()

import json
import pytest
from django.http import JsonResponse
from django.http import HttpRequest
from unittest.mock import MagicMock, patch
from django.contrib.auth.models import User
from backend.views.note_views import create_or_update_note, delete_note
from backend.services.note_service import NoteService

@pytest.fixture
def error_fixture():
    return ValueError("Error fixture")

@pytest.fixture
def authenticated_user():
    user = User(id=1, username='user_de_prueba', password='password123')
    return user

def test_create_note_success(authenticated_user):
    content = "test content"
    status_id = 1
    data = {'content': content, 'status_id': status_id}
    request = HttpRequest()
    request.method = 'POST'
    request.user = authenticated_user
    request._body = json.dumps(data).encode('utf-8')

    with patch.object(NoteService, 'create_note', side_effect=None) as mock_create_note:

        response = create_or_update_note(request)

        assert mock_create_note.called
        assert response.status_code == 200
        assert response.content == JsonResponse({"Message": "Se creo la nota con exito"}).content

def test_create_note_fail(authenticated_user, error_fixture):
    content = "test content"
    status_id = 1
    data = {'content': content, 'status_id': status_id}
    request = HttpRequest()
    request.method = 'POST'
    request.user = authenticated_user
    request._body = json.dumps(data).encode('utf-8')

    with patch.object(NoteService, 'create_note', side_effect=error_fixture) as mock_create_note:

        response = create_or_update_note(request)

        assert mock_create_note.called
        assert response.status_code == 400
        assert response.content == JsonResponse({"error": "Ocurrio un error al intentar crear una nota."}).content

def test_update_note_success(authenticated_user):
    content = "test content"
    status_id = 1
    note_id = 1
    data = {'content': content, 'status_id': status_id, 'note_id': note_id}
    request = HttpRequest()
    request.method = 'PUT'
    request.user = authenticated_user
    request._body = json.dumps(data).encode('utf-8')

    with patch.object(NoteService, 'update_note', side_effect=None) as mock_update_note:

        response = create_or_update_note(request)

        assert mock_update_note.called
        assert response.status_code == 200
        assert response.content == JsonResponse({"Message":"Se actualizo la nota con exito"}).content


def test_update_note_fail(authenticated_user, error_fixture):
    content = "test content"
    status_id = 1
    note_id = 1
    data = {'content': content, 'status_id': status_id, 'note_id': note_id}
    request = HttpRequest()
    request.method = 'PUT'
    request.user = authenticated_user
    request._body = json.dumps(data).encode('utf-8')

    with patch.object(NoteService, 'update_note', side_effect=error_fixture) as mock_update_note:

        response = create_or_update_note(request)

        assert mock_update_note.called
        assert response.status_code == 400
        assert response.content == JsonResponse({'error': 'Ocurrio un error al intentar actualizar una nota.'}).content


def test_delete_note_success(authenticated_user):
    request = HttpRequest()
    request.method = 'DELETE'
    request.user = authenticated_user

    with patch.object(NoteService, 'delete_note', side_effect=None) as mock_update_note:

        response = delete_note(request, 1)

        assert mock_update_note.called
        assert response.status_code == 200
        assert response.content == JsonResponse({"Message":"Se eliminó la nota con exito"}).content

def test_delete_note_fail(authenticated_user, error_fixture):
    request = HttpRequest()
    request.method = 'DELETE'
    request.user = authenticated_user

    with patch.object(NoteService, 'delete_note', side_effect=error_fixture) as mock_update_note:

        response = delete_note(request, 1)

        assert mock_update_note.called
        assert response.status_code == 400
        assert response.content == JsonResponse({'error': 'Ocurrio un error al intentar eliminar una nota.'}).content
