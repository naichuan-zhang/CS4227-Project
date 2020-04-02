from rest_framework import routers
from .api import OrderViewSet


# Register views in ViewSet
router = routers.DefaultRouter()
router.register('api/order', OrderViewSet, 'order')

urlpatterns = router.urls
