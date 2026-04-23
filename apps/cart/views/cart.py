from rest_framework.viewsets import ModelViewSet
from apps.cart.models import Cart
from apps.cart.serializers.cart import CartSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer