from rest_framework.viewsets import ModelViewSet
from apps.catalog.models import Material
from apps.catalog.serializers.material import MaterialSerializer


class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer