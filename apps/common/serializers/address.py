from parler_rest.serializers import TranslatableModelSerializer
from apps.common.models import Address


class AddressSerializer(TranslatableModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"