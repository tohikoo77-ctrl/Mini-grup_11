from rest_framework.viewsets import ModelViewSet
from apps.payments.models import TopUp
from apps.payments.serializers.top_up import TopUpSerializer
from apps.payments.filters import TopUpFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class TopUpViewSet(ModelViewSet):
    queryset = TopUp.objects.all()
    serializer_class = TopUpSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = TopUpFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'
