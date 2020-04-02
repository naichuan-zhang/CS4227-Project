from rest_framework import routers
from .api import OrderViewSet, CartViewSet, ItemViewSet, OrderItemViewSet


# Register views in ViewSet
router = routers.DefaultRouter()
router.register('api/order', OrderViewSet, 'order')
router.register('api/cart', CartViewSet, 'cart')
router.register('api/item', ItemViewSet, 'item')
router.register('api/orderitem', OrderItemViewSet, 'orderitem')

urlpatterns = router.urls
