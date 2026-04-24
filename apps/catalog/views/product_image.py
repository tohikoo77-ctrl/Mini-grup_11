from rest_framework.viewsets import ModelViewSet
from apps.catalog.models import ProductImage
from apps.catalog.serializers.product_image import ProductImageSerializer
from apps.catalog.filters import ProductImageFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class ProductImageViewSet(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductImageFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'