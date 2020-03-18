from order.composite.itemcomponent import ItemComponent
from order.models import Item


class ItemLeaf(ItemComponent):
    """Composite Leaf"""

    def __init__(self, item: Item, amount: int):
        self._item = item
        self._amount = amount

    def get_price(self):
        return self._item.price * self._amount

    def get_name(self):
        return self._item.name + " x" + str(self._amount)
