from decimal import Decimal
from typing import List

from order.composite.itemcomponent import ItemComponent
from order.models import Order


class ItemComposite(ItemComponent):
    """Composite"""

    def __init__(self):
        self._items: List[ItemComponent] = list()

    def get_price(self):
        price: Decimal = Decimal('0.0')
        for item in self._items:
            price += item.get_price()
        return price

    def create_order_item(self, order: Order):
        for item in self._items:
            item.create_order_item(order)

    def add(self, item: ItemComponent):
        self._items.append(item)

    def remove(self, item: ItemComponent):
        self._items.remove(item)
