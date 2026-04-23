from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.wish import WishViewSet
from .views.cart import CartViewSet
from .views.cart_item import CartItemViewSet

router = DefaultRouter()
router.register(r"wishes", WishViewSet, basename="wish")
router.register(r"carts", CartViewSet, basename="cart")
router.register(r"cart-items", CartItemViewSet, basename="cart-item")

urlpatterns = [
    path("", include(router.urls)),
]