from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from apps.cart.models import CartItem
from apps.cart.serializers.cart_item import CartItemSerializer
from apps.cart.filters import CartItemFilter


class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CartItemFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'