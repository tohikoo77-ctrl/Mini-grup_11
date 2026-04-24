from rest_framework.viewsets import ModelViewSet
from apps.catalog.models import Material
from apps.catalog.serializers.material import MaterialSerializer
from apps.catalog.filters import MaterialFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MaterialFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'