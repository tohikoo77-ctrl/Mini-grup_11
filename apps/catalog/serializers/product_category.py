from parler_rest.serializers import TranslatableModelSerializer
from apps.catalog.models import ProductCategory


class ProductCategorySerializer(TranslatableModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"