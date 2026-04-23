from rest_framework.viewsets import ModelViewSet
from apps.content.models import Publication
from apps.content.serializers.publication import PublicationSerializer


class PublicationViewSet(ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer