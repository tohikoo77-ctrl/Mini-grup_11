from parler_rest.serializers import TranslatableModelSerializer
from apps.catalog.models import Color


class ColorSerializer(TranslatableModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"