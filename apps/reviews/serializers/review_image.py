from rest_framework import serializers
from apps.reviews.models import ReviewImage


class ReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewImage
        fields = "__all__"
