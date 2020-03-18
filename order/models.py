from enum import IntEnum
from django.db import models
from user.models import User


class ItemTypeEnum(IntEnum):
    MAIN = 0
    SIDE = 1
    DRINK = 2

    @classmethod
    def tuples(cls):
        return tuple((state.name, state.value) for state in cls)


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=20, choices=ItemTypeEnum.tuples(), default=ItemTypeEnum.MAIN)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=100)

    @staticmethod
    def get_types():
        return Item.objects.order_by().values_list('type', flat=True).distinct()

    @staticmethod
    def get_items_by_type(type_):
        return Item.objects.filter(type=type_)

    def __str__(self):
        return self.name


class OrderStateEnum(IntEnum):
    PENDING = 0
    ORDERED = 1
    CANCELLED = 2
    COMPLETED = 3

    @classmethod
    def tuples(cls): return tuple((state.name, state.value) for state in cls)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=20, choices=OrderStateEnum.tuples(), default=OrderStateEnum.PENDING)

    def order(self):
        self.state = OrderStateEnum.ORDERED

    def cancel(self):
        self.state = OrderStateEnum.CANCELLED

    def complete(self):
        self.state = OrderStateEnum.COMPLETED

    def __str__(self):
        return str(self.id) + ' ' + str(self.state)


class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    ord_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)


