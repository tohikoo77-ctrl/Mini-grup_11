from rest_framework.viewsets import ModelViewSet
from apps.notifications.models import UserNotification
from apps.notifications.serializers.user_notification import UserNotificationSerializer
from apps.notifications.filters import UserNotificationFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class UserNotificationViewSet(ModelViewSet):
    queryset = UserNotification.objects.all()
    serializer_class = UserNotificationSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = UserNotificationFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'