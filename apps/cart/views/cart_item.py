from rest_framework.viewsets import ModelViewSet
from apps.cart.models import CartItem
from apps.cart.serializers.cart_item import CartItemSerializer


class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer