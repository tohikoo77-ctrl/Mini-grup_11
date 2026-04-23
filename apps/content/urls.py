from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.publication import PublicationViewSet
from .views.publication_category import PublicationCategoryViewSet

router = DefaultRouter()
router.register(r"publications", PublicationViewSet, basename="publication")
router.register(r"publication-categories", PublicationCategoryViewSet, basename="publication-category")

urlpatterns = [
    path("", include(router.urls)),
]