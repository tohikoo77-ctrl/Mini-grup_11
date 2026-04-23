from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.promotion import PromotionViewSet
from .views.newsletter_subscriber import NewsletterSubscriberViewSet
from .views.discount_threshold import DiscountThresholdViewSet

router = DefaultRouter()
router.register(r"promotions", PromotionViewSet, basename="promotion")
router.register(r"newsletter-subscribers", NewsletterSubscriberViewSet, basename="newsletter-subscriber")
router.register(r"discount-thresholds", DiscountThresholdViewSet, basename="discount-threshold")

urlpatterns = [
    path("", include(router.urls)),
]