from rest_framework.viewsets import ModelViewSet
from apps.content.models import Publication
from apps.content.serializers.publication import PublicationSerializer
from apps.content.filters import PublicationFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class PublicationViewSet(ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PublicationFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'