from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.promotion_category import PromotionCategoryViewSet
from .views.promotion import PromotionViewSet
from .views.wallet import WalletViewSet
from .views.top_up import TopUpViewSet
from .views.payment import PaymentViewSet
from .views.payment_type import PaymentTypeViewSet
from .views.card import CardViewSet

router = DefaultRouter()
router.register(r"promotion-categories", PromotionCategoryViewSet, basename="promotion-category")
router.register(r"promotions", PromotionViewSet, basename="promotion")
router.register(r"wallets", WalletViewSet, basename="wallet")
router.register(r"top-ups", TopUpViewSet, basename="top-up")
router.register(r"payments", PaymentViewSet, basename="payment")
router.register(r"payment-types", PaymentTypeViewSet, basename="payment-type")
router.register(r"cards", CardViewSet, basename="card")

app_name = "payments"

urlpatterns = [
    path("", include(router.urls)),
]
