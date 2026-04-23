from rest_framework import serializers
from apps.marketing.models import DiscountThreshold


class DiscountThresholdSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountThreshold
        fields = "__all__"