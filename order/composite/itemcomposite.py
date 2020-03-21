from typing import List

from order.composite.itemcomponent import ItemComponent


class ItemComposite(ItemComponent):
    """Composite"""

    def __init__(self):
        # self._title = title
        self._items: List[ItemComponent] = list()

    def get_price(self):
        price: float = 0.0
        for item in self._items:
            price += float(item.get_price())
        return price

    # def get_name(self):
    #     items = "*** " + self._title + " ***"
    #     for item in self._items:
    #         items += " + " + item.get_name()
    #     items += " "
    #     return items

    def add(self, item: ItemComponent):
        self._items.append(item)

    def remove(self, item: ItemComponent):
        self._items.remove(item)
