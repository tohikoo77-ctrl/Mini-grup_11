from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField
from apps.payments.models import PromotionCategory


class PromotionCategorySerializer(TranslatableModelSerializer):
    """Full serializer with translations"""
    translations = TranslatedFieldsField(shared_model=PromotionCategory)

    class Meta:
        model = PromotionCategory
        fields = [
            'id',
            'slug',
            'color',
            'icon',
            'is_active',
            'display_order',
            'translations',
            'created',
            'modified',
        ]
        read_only_fields = ['id', 'created', 'modified']


class PromotionCategoryListSerializer(TranslatableModelSerializer):
    """Simplified serializer for listing categories (returns current/any translation)"""
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = PromotionCategory
        fields = [
            'id',
            'slug',
            'name',
            'description',
            'color',
            'icon',
            'is_active',
            'display_order',
        ]

    def get_name(self, obj):
        return obj.safe_translation_getter("name", any_language=True)

    def get_description(self, obj):
        return obj.safe_translation_getter("description", any_language=True)
