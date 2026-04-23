from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.product import ProductViewSet
from .views.product_image import ProductImageViewSet
from .views.product_category import ProductCategoryViewSet
from .views.material import MaterialViewSet
from .views.color import ColorViewSet
from .views.brand import BrandViewSet

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="product")
router.register(r"product-images", ProductImageViewSet, basename="product-image")
router.register(r"product-categories", ProductCategoryViewSet, basename="product-category")
router.register(r"materials", MaterialViewSet, basename="material")
router.register(r"colors", ColorViewSet, basename="color")
router.register(r"brands", BrandViewSet, basename="brand")

urlpatterns = [
    path("", include(router.urls)),
]