from order.composite.itemcomponent import ItemComponent
from order.models import Item, Order, OrderItem


class ItemLeaf(ItemComponent):
    """Composite Leaf"""

    def __init__(self, item: Item, amount: int):
        self._item = item
        self._amount = amount

    def get_price(self):
        return self._item.price * self._amount

    def create_order_item(self, order: Order):
        order_item = OrderItem(item=self._item, order=order, amount=self._amount)
        order_item.save()
