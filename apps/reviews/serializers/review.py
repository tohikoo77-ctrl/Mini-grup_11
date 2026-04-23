from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from apps.reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

    def validate(self, attrs):
        if attrs.get("rating", 0) < 1 or attrs.get("rating", 0) > 5:
            raise serializers.ValidationError(_("Rating must be between 1 and 5"))
        return attrs
