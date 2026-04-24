from rest_framework.viewsets import ModelViewSet
from apps.reviews.models import ReviewImage
from apps.reviews.serializers.review_image import ReviewImageSerializer
from apps.reviews.filters import ReviewImageFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class ReviewImageViewSet(ModelViewSet):
    queryset = ReviewImage.objects.all()
    serializer_class = ReviewImageSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ReviewImageFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'