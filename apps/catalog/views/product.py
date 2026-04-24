from rest_framework.viewsets import ModelViewSet
from apps.catalog.models import Product
from apps.catalog.serializers.product import ProductSerializer
from apps.catalog.filters import ProductFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'