from rest_framework.viewsets import ModelViewSet
from apps.cart.models import Cart
from apps.cart.serializers.cart import CartSerializer
from apps.cart.filters import CartFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CartFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'
