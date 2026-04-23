from rest_framework.viewsets import ModelViewSet
from apps.cart.models import Wish
from apps.cart.serializers.wish import WishSerializer


class WishViewSet(ModelViewSet):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer