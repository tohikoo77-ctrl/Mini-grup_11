from rest_framework.viewsets import ModelViewSet
from apps.catalog.models import Brand
from apps.catalog.serializers.brand import BrandSerializer
from apps.catalog.filters import BrandFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BrandFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'