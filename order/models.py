from enum import IntEnum
from django.db import models

from order.strategy.strategy import Strategy
from order.visitor.visitable import Visitable
from user.models import User


class ItemTypeEnum(IntEnum):
    STARTER = 0
    MAIN = 1
    DESSERT = 2
    DRINK = 3

    @classmethod
    def tuples(cls):
        return tuple((state.name, state.value) for state in cls)


class Item(Visitable):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=20, choices=ItemTypeEnum.tuples(), default=ItemTypeEnum.STARTER)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=100)

    @staticmethod
    def get_types():
        return Item.objects.order_by().values_list('type', flat=True).distinct()

    @staticmethod
    def get_items_by_type(type_):
        return Item.objects.filter(type=type_)

    def get_name(self):
        return str(self.name)

    def get_price(self):
        return self.price

    def __str__(self):
        return str(self.name)

    def accept(self, visitor):
        return visitor.visit(self)


class Cart(Visitable):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    num = models.IntegerField(default=1)
    is_selected = models.BooleanField(default=True)

    def accept(self, visitor):
        return visitor.visit(self)


class OrderStateEnum(IntEnum):
    PENDING = 0
    ORDERED = 1
    CANCELLED = 2
    COMPLETED = 3

    @classmethod
    def tuples(cls): return tuple((state.name, state.value) for state in cls)


class Order(Visitable):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.FloatField(default=0.0)
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

    def accept(self, visitor):
        return visitor.visit(self)


class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)

class PayCard(models.Model):

    name = models.CharField(max_length=30)
    card = models.IntegerField()

    class Meta:
        db_table = 'pay_card'


class PayPal(models.Model):

    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    class Meta:
        db_table = 'paypal'
