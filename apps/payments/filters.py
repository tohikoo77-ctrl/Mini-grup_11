from apps.payments.models import Card, PaymentType, Payment, PromotionCategory, Promotion, TopUp, Wallet
from apps.shared.filters import make_filter

CardFilter = make_filter(Card)
PaymentTypeFilter = make_filter(PaymentType)
PaymentFilter = make_filter(Payment)
PromotionCategoryFilter = make_filter(PromotionCategory)
PromotionFilter = make_filter(Promotion)
TopUpFilter = make_filter(TopUp)
WalletFilter = make_filter(Wallet)
