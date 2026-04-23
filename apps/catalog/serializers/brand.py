from parler_rest.serializers import TranslatableModelSerializer
from apps.catalog.models import Brand


class BrandSerializer(TranslatableModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"