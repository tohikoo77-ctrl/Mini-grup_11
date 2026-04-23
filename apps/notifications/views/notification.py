from rest_framework.viewsets import ModelViewSet
from apps.notifications.models import Notification
from apps.notifications.serializers.notification import NotificationSerializer


class NotificationViewSet(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer