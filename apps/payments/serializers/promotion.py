from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField
from apps.payments.models import Promotion, PromotionCategory
from .promotion_category import PromotionCategoryListSerializer


class PromotionSerializer(TranslatableModelSerializer):
    """Full serializer with translations"""
    translations = TranslatedFieldsField(shared_model=Promotion)
    category = PromotionCategoryListSerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=PromotionCategory.objects.filter(is_active=True),
        source="category",
        write_only=True,
    )
    is_active = serializers.ReadOnlyField()
    discount_display = serializers.ReadOnlyField()

    class Meta:
        model = Promotion
        fields = [
            "id",
            "code",
            "category",
            "category_id",
            "discount_type",
            "discount_value",
            "discount_display",
            "valid_from",
            "valid_to",
            "minimum_spend",
            "usage_limit",
            "used_count",
            "is_featured",
            "is_active",
            "display_order",
            "translations",
            "created",
            "modified",
        ]
        read_only_fields = ["id", "used_count", "created", "modified"]


class PromotionListSerializer(TranslatableModelSerializer):
    """Simplified serializer for listing promotions (returns current/any translation)"""
    title = serializers.SerializerMethodField()
    subtitle = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    category = PromotionCategoryListSerializer(read_only=True)
    is_active = serializers.ReadOnlyField()
    discount_display = serializers.ReadOnlyField()

    class Meta:
        model = Promotion
        fields = [
            "id",
            "code",
            "title",
            "subtitle",
            "description",
            "category",
            "discount_type",
            "discount_value",
            "discount_display",
            "valid_from",
            "valid_to",
            "minimum_spend",
            "usage_limit",
            "used_count",
            "is_featured",
            "is_active",
            "display_order",
        ]

    def get_title(self, obj):
        return obj.safe_translation_getter("title", any_language=True)

    def get_subtitle(self, obj):
        return obj.safe_translation_getter("subtitle", any_language=True)

    def get_description(self, obj):
        return obj.safe_translation_getter("description", any_language=True)


class PromotionApplySerializer(serializers.ModelSerializer):
    """Serializer for applying promotions (validation only)"""

    class Meta:
        model = Promotion
        fields = ["code"]

    def validate_code(self, value):
        """Validate promotion code and check if it's applicable"""
        try:
            promotion = Promotion.objects.get(code=value)
        except Promotion.DoesNotExist:
            raise serializers.ValidationError("Invalid promotion code.")

        if not promotion.is_active:
            raise serializers.ValidationError("This promotion is no longer active.")

        return value
