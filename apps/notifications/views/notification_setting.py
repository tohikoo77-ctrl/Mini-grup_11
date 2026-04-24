from rest_framework.viewsets import ModelViewSet
from apps.notifications.models import NotificationSetting
from apps.notifications.serializers.notification_setting import NotificationSettingSerializer
from apps.notifications.filters import NotificationSettingFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class NotificationSettingViewSet(ModelViewSet):
    queryset = NotificationSetting.objects.all()
    serializer_class = NotificationSettingSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = NotificationSettingFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'