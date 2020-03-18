from order.composite.itemcomponent import ItemComponent
from order.models import Item


class ItemLeaf(ItemComponent):
    """Composite Leaf"""

    def __init__(self, item: Item):
        self._item = item

    def get_price(self):
        return self._item.name

    def get_name(self):
        return self._item.price
