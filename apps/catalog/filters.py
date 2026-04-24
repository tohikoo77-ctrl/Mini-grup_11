from apps.catalog.models import Brand, Color, Material, ProductCategory, ProductImage, Product
from apps.shared.filters import make_filter


BrandFilter = make_filter(Brand)
ColorFilter = make_filter(Color)
MaterialFilter = make_filter(Material)
ProductCategoryFilter = make_filter(ProductCategory)
ProductImageFilter = make_filter(ProductImage)
ProductFilter = make_filter(Product)
