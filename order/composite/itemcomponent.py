from abc import ABC, abstractmethod

from order.models import Order


class ItemComponent(ABC):
    """Composite Interface"""

    @abstractmethod
    def get_price(self):
        raise NotImplementedError("You should implement this.")

    @abstractmethod
    def create_order_item(self, order: Order):
        raise NotImplementedError("You should implement this.")
