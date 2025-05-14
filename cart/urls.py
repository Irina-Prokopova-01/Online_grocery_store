from django.urls import path, include
# from rest_framework.routers import SimpleRouter
from rest_framework.routers import DefaultRouter
from .apps import CartConfig
from cart.views import CartViewSet, CartItemViewSet

app_name = CartConfig.name

router = DefaultRouter()
router.register(r"cart", CartViewSet, basename="cart")
router.register(r"cart-items", CartItemViewSet)


urlpatterns = [
    path("", include(router.urls)),
    # path("cart/create/", CartViewSet.as_view({'create': 'create'}), name="cart-create"),
    path("cart/clear/", CartViewSet.as_view({'delete': 'clear'}), name="clear-cart")
]

urlpatterns += router.urls



