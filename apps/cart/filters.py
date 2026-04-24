from apps.cart.models import Cart, CartItem, Wish
from apps.shared.filters import make_filter


CartFilter = make_filter(Cart)
CartItemFilter = make_filter(CartItem)
WishFilter = make_filter(Wish)
