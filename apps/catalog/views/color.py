from rest_framework.viewsets import ModelViewSet
from apps.catalog.models import Color
from apps.catalog.serializers.color import ColorSerializer


class ColorViewSet(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer