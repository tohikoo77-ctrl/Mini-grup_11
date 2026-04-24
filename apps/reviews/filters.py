from apps.reviews.models import Review, ReviewImage
from apps.shared.filters import make_filter

ReviewFilter = make_filter(Review)
ReviewImageFilter = make_filter(ReviewImage)
