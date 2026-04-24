from apps.marketing.models import Promotion, DiscountThreshold, NewsletterSubscriber
from apps.shared.filters import make_filter

PromotionFilter = make_filter(Promotion)
DiscountThresholdFilter = make_filter(DiscountThreshold)
NewsletterSubscriberFilter = make_filter(NewsletterSubscriber)
