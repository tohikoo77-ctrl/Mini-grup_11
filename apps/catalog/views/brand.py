from rest_framework.viewsets import ModelViewSet
from apps.catalog.models import Brand
from apps.catalog.serializers.brand import BrandSerializer


class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer