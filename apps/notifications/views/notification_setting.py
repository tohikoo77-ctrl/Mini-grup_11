from rest_framework.viewsets import ModelViewSet
from apps.notifications.models import NotificationSetting
from apps.notifications.serializers.notification_setting import NotificationSettingSerializer


class NotificationSettingViewSet(ModelViewSet):
    queryset = NotificationSetting.objects.all()
    serializer_class = NotificationSettingSerializer