from order.models import Order
from rest_framework import viewsets, permissions
from .serializers import OrderSerializer


# Controller for request
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = OrderSerializer
