from rest_framework.viewsets import ModelViewSet
from apps.payments.models import Wallet
from apps.payments.serializers.wallet import WalletSerializer


class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
