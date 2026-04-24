from rest_framework.viewsets import ModelViewSet
from apps.catalog.models import ProductCategory
from apps.catalog.serializers.product_category import ProductCategorySerializer
from apps.catalog.filters import ProductCategoryFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class ProductCategoryViewSet(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductCategoryFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'