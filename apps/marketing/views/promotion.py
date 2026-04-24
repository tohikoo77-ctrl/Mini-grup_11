from rest_framework.viewsets import ModelViewSet
from apps.marketing.models import Promotion
from apps.marketing.serializers.promotion import PromotionSerializer
from apps.marketing.filters import PromotionFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class PromotionViewSet(ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PromotionFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'