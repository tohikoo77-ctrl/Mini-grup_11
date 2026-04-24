from rest_framework.viewsets import ModelViewSet
from apps.catalog.models import Color
from apps.catalog.serializers.color import ColorSerializer
from apps.catalog.filters import ColorFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class ColorViewSet(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ColorFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'