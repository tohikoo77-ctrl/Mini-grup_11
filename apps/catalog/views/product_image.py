from rest_framework.viewsets import ModelViewSet
from apps.catalog.models import ProductImage
from apps.catalog.serializers.product_image import ProductImageSerializer


class ProductImageViewSet(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer