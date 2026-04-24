from rest_framework.viewsets import ModelViewSet
from apps.notifications.models import Notification
from apps.notifications.serializers.notification import NotificationSerializer
from apps.notifications.filters import NotificationFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class NotificationViewSet(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = NotificationFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'