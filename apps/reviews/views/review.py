from rest_framework.viewsets import ModelViewSet
from apps.reviews.models import Review
from apps.reviews.serializers.review import ReviewSerializer
from apps.reviews.filters import ReviewFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ReviewFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'
