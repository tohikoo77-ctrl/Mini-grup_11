from parler_rest.serializers import TranslatableModelSerializer
from apps.catalog.models import Product


class ProductSerializer(TranslatableModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"