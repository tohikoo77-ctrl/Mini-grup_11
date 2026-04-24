from apps.content.models import Publication, PublicationCategory
from apps.shared.filters import make_filter

PublicationFilter = make_filter(Publication)
PublicationCategoryFilter = make_filter(PublicationCategory)
