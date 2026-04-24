from rest_framework.viewsets import ModelViewSet
from apps.payments.models import Card
from apps.payments.serializers.card import CardSerializer
from apps.payments.filters import CardFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CardFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'