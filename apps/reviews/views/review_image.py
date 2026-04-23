from rest_framework.viewsets import ModelViewSet
from apps.reviews.models import ReviewImage
from apps.reviews.serializers.review_image import ReviewImageSerializer


class ReviewImageViewSet(ModelViewSet):
    queryset = ReviewImage.objects.all()
    serializer_class = ReviewImageSerializer
