from rest_framework import serializers
from apps.reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

    def validate(self, attrs):
        if attrs["rating"] < 1 or attrs["rating"] > 5:
            raise serializers.ValidationError(_("Rating must be between 1 and 5"))
        return attrs
