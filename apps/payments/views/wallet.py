from rest_framework.viewsets import ModelViewSet
from apps.payments.models import Wallet
from apps.payments.serializers.wallet import WalletSerializer
from apps.payments.filters import WalletFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class WalletViewSet(ModelViewSet):
    """ViewSet for managing wallets."""
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = WalletFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'
