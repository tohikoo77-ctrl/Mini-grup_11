from parler_rest.serializers import TranslatableModelSerializer
from apps.content.models import Publication


class PublicationSerializer(TranslatableModelSerializer):
    class Meta:
        model = Publication
        fields = "__all__"