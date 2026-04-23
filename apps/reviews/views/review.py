from rest_framework.viewsets import ModelViewSet
from apps.reviews.models import Review
from apps.reviews.serializers.review import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
