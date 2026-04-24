from rest_framework.viewsets import ModelViewSet
from apps.common.models import Address
from apps.common.serializers.address import AddressSerializer
from apps.common.filters import AddressFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = AddressFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'
