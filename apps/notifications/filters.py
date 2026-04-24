from apps.notifications.models import Notification, NotificationSetting, UserNotification
from apps.shared.filters import make_filter

NotificationFilter = make_filter(Notification)
NotificationSettingFilter = make_filter(NotificationSetting)
UserNotificationFilter = make_filter(UserNotification)
