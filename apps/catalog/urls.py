from django.urls import path
from .views import ProductCategoryView, ProductView

urlpatterns = [
    path("ctg/", ProductCategoryView.as_view()),
    path("ctg/<int:pk>/", ProductCategoryView.as_view()),

    path("product/", ProductView.as_view()),
]