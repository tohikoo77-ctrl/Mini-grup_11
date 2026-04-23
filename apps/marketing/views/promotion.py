from rest_framework.viewsets import ModelViewSet
from apps.marketing.models import Promotion
from apps.marketing.serializers.promotion import PromotionSerializer


class PromotionViewSet(ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer