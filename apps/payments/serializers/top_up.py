from rest_framework import serializers
from apps.payments.models import TopUp


class TopUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopUp
        fields = "__all__"
