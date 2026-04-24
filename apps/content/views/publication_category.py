from rest_framework.viewsets import ModelViewSet
from apps.content.models import PublicationCategory
from apps.content.serializers.publication_category import PublicationCategorySerializer
from apps.content.filters import PublicationCategoryFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class PublicationCategoryViewSet(ModelViewSet):
    queryset = PublicationCategory.objects.all()
    serializer_class = PublicationCategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PublicationCategoryFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'