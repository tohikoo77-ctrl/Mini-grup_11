from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.payments.filters import PromotionCategoryFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from apps.payments.models import PromotionCategory
from apps.payments.serializers.promotion_category import (
    PromotionCategorySerializer,
    PromotionCategoryListSerializer,
)


class PromotionCategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for managing promotion categories."""
    queryset = PromotionCategory.objects.all()
    serializer_class = PromotionCategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PromotionCategoryFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'

    def get_serializer_class(self):
        if self.action == "list":
            return PromotionCategoryListSerializer
        return PromotionCategorySerializer

    @action(detail=False, methods=["get"])
    def active(self, request):
        """Get only active categories"""
        qs = self.get_queryset().filter(is_active=True)
        serializer = PromotionCategoryListSerializer(qs, many=True, context={"request": request})
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def promotions(self, request, pk=None):
        """Get promotions under this category"""
        category = self.get_object()
        promotions = category.promotions.all()
        from apps.payments.serializers.promotion import PromotionListSerializer
        serializer = PromotionListSerializer(promotions, many=True, context={"request": request})
        return Response(serializer.data)
