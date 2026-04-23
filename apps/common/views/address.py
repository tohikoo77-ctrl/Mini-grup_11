from rest_framework.viewsets import ModelViewSet
from apps.common.models import Address
from apps.common.serializers.address import AddressSerializer


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer