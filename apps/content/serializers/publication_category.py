from parler_rest.serializers import TranslatableModelSerializer
from apps.content.models import PublicationCategory


class PublicationCategorySerializer(TranslatableModelSerializer):
    class Meta:
        model = PublicationCategory
        fields = "__all__"