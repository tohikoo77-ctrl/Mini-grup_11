from rest_framework.viewsets import ModelViewSet
from apps.catalog.models import ProductCategory
from apps.catalog.serializers.product_category import ProductCategorySerializer


class ProductCategoryViewSet(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer