from rest_framework import serializers
from apps.notifications.models import NotificationSetting


class NotificationSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationSetting
        fields = "__all__"