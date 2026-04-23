from parler_rest.serializers import TranslatableModelSerializer
from apps.catalog.models import Material


class MaterialSerializer(TranslatableModelSerializer):
    class Meta:
        model = Material
        fields = "__all__"