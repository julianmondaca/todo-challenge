from django.utils.dateparse import parse_datetime
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django_filters import FilterSet, CharFilter
from django_filters import rest_framework as filters
from backend.models import Note
from backend.views.api.serializers import NoteSerializer

class NoteFilter(FilterSet):
    content = CharFilter(field_name='content', lookup_expr='icontains')
    class Meta:
        model = Note
        fields = ['content']

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.filter(date_deleted__isnull=True).order_by('date_created')
    serializer_class = NoteSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = NoteFilter
    ordering_fields = ['date_created', 'date_updated']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        date_str = self.request.query_params.get('date', None)
        if date_str:
            date = parse_datetime(date_str)
            if date:
                queryset = queryset.filter(date_created__date=date)
        queryset = queryset.prefetch_related('status')
        
        return queryset
