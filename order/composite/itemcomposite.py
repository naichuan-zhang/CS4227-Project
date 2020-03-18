from typing import List

from order.composite.itemcomponent import ItemComponent


class ItemComposite(ItemComponent):
    """Composite"""

    def __init__(self, title):
        self._title = title
        self._items: List[ItemComponent] = list()

    def get_price(self):
        price = 0
        for item in self._items:
            price += item.get_price()
        return price

    def get_name(self):
        items = "*** " + self._title + " ***"
        items += "<br>"
        for item in self._items:
            items += "<br>" + item.get_name()
        return items

    def add(self, item: ItemComponent):
        self._items.append(item)

    def remove(self, item: ItemComponent):
        self._items.remove(item)
