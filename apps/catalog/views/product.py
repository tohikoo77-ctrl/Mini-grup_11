from rest_framework.viewsets import ModelViewSet
from apps.catalog.models import Product
from apps.catalog.serializers.product import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer