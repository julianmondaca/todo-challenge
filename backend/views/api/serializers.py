from rest_framework import serializers
from backend.models import Note, Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'status']

class NoteSerializer(serializers.ModelSerializer):
    status = StatusSerializer()

    class Meta:
        model = Note
        fields = ['id', 'content', 'date_created', 'date_updated', 'status']