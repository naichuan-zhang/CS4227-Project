from rest_framework import serializers
from order.models import Order


# Convert complex data (e.g. Models) into Python datatypes
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
