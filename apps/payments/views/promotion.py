from django.db import models
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from apps.payments.filters import PromotionFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from apps.payments.models import Promotion
from apps.payments.serializers.promotion import (
    PromotionSerializer,
    PromotionListSerializer,
    PromotionApplySerializer,
)


class PromotionViewSet(viewsets.ModelViewSet):
    """ViewSet for managing promotions"""

    queryset = Promotion.objects.all().select_related("category")
    serializer_class = PromotionSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PromotionFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'

    def get_serializer_class(self):
        if self.action == "list":
            return PromotionListSerializer
        if self.action == "apply":
            return PromotionApplySerializer
        return PromotionSerializer

    # ---------- Extra actions ----------

    @action(detail=False, methods=["get"])
    def featured(self, request):
        """Get featured promotions"""
        qs = self.get_queryset().filter(is_featured=True)
        serializer = PromotionListSerializer(qs, many=True, context={"request": request})
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def active(self, request):
        """Get currently active promotions"""
        now = timezone.now()
        qs = self.get_queryset().filter(
            valid_from__lte=now, valid_to__gte=now
        ).exclude(usage_limit__lte=models.F("used_count"))
        serializer = PromotionListSerializer(qs, many=True, context={"request": request})
        return Response(serializer.data)

    @action(detail=False, methods=["post"])
    def apply(self, request):
        """Validate and apply a promotion code"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        promotion = Promotion.objects.get(code=serializer.validated_data["code"])
        return Response(
            {
                "id": promotion.id,
                "code": promotion.code,
                "discount_display": promotion.discount_display,
                "is_active": promotion.is_active,
            },
            status=status.HTTP_200_OK,
        )

    @action(detail=True, methods=["post"])
    def use(self, request, pk=None):
        """Mark promotion as used"""
        promotion = self.get_object()
        if promotion.usage_limit and promotion.used_count >= promotion.usage_limit:
            return Response(
                {"detail": "Usage limit reached."}, status=status.HTTP_400_BAD_REQUEST
            )
        promotion.used_count += 1
        promotion.save(update_fields=["used_count"])
        return Response({"detail": "Promotion marked as used."})

    @action(detail=False, methods=["get"], url_path="by_category")
    def by_category(self, request):
        """Group promotions by category"""
        categories = {}
        for promo in self.get_queryset():
            cat = promo.category.safe_translation_getter("name", any_language=True)
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(PromotionListSerializer(promo, context={"request": request}).data)
        return Response(categories)
