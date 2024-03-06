"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from backend.views.note_views import create_or_update_note, delete_note
from rest_framework.routers import DefaultRouter
from backend.views.api.viewsets import NoteViewSet
from backend.views.api.login_viewset import LoginViewSet
router = DefaultRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', create_or_update_note, name='create_or_update_note'),
    path('notes/<int:note_id>/', delete_note, name='delete_note'),
    path('api/', include(router.urls)),
    path('login/', LoginViewSet.as_view(), name='login'),
]
