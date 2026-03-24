from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.promotion_category import PromotionCategoryViewSet
from .views.promotion import PromotionViewSet

router = DefaultRouter()
# top-level categories
router.register(r'promotion-categories', PromotionCategoryViewSet, basename='promotion-category')
# promotions that belong to categories
router.register(r'promotions', PromotionViewSet, basename='promotion')

app_name = "payments"

urlpatterns = [
    path("", include(router.urls)),
]
