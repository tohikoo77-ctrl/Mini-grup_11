from rest_framework.viewsets import ModelViewSet
from apps.marketing.models import DiscountThreshold
from apps.marketing.serializers.discount_threshold import DiscountThresholdSerializer
from apps.marketing.filters import DiscountThresholdFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class DiscountThresholdViewSet(ModelViewSet):
    queryset = DiscountThreshold.objects.all()
    serializer_class = DiscountThresholdSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = DiscountThresholdFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'