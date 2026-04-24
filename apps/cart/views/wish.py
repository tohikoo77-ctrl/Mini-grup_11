from rest_framework.viewsets import ModelViewSet
from apps.cart.models import Wish
from apps.cart.serializers.wish import WishSerializer
from apps.cart.filters import WishFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class WishViewSet(ModelViewSet):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = WishFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'
