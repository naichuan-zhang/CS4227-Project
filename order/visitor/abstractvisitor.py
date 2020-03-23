from abc import ABC, abstractmethod
from functools import singledispatch
from typing import TYPE_CHECKING

from order.models import Order, Cart, Item
from order.visitor.visitable import Visitable

if TYPE_CHECKING:
    from order.models import Order, Cart, Item
    from order.visitor.visitable import Visitable


class AbstractVisitor(ABC):
    def __init__(self) -> None:
        super().__init__()

        from order.models import Order, Cart, Item

        self.visit = singledispatch(self.visit)
        self.visit.register(Order, self._visit_order)
        self.visit.register(Cart, self._visit_cart)
        self.visit.register(Item, self._visit_item)

    def visit(self, element: Visitable):
        raise NotImplementedError

    @abstractmethod
    def _visit_order(self, element: Order):
        raise NotImplementedError

    @abstractmethod
    def _visit_cart(self, element: Cart):
        raise NotImplementedError

    @abstractmethod
    def _visit_item(self, element: Item):
        raise NotImplementedError

