from rest_framework.viewsets import ModelViewSet
from apps.marketing.models import DiscountThreshold
from apps.marketing.serializers.discount_threshold import DiscountThresholdSerializer


class DiscountThresholdViewSet(ModelViewSet):
    queryset = DiscountThreshold.objects.all()
    serializer_class = DiscountThresholdSerializer