from rest_framework.viewsets import ModelViewSet
from apps.content.models import PublicationCategory
from apps.content.serializers.publication_category import PublicationCategorySerializer


class PublicationCategoryViewSet(ModelViewSet):
    queryset = PublicationCategory.objects.all()
    serializer_class = PublicationCategorySerializer