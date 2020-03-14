from abc import ABC, abstractmethod

from order.models import Order


class AbstractOrderOrderService(ABC):
    @abstractmethod
    def create_order(self, order: Order) -> Order:
        raise NotImplementedError("You have to implement this")


class OrderOrderService(AbstractOrderOrderService):
    def create_order(self, order: Order) -> Order:
        # TODO: Interact with database here
        return order


class AbstractCancelOrderService(ABC):
    @abstractmethod
    def cancel_order(self, order: Order) -> Order:
        raise NotImplementedError("You have to implement this")


class CancelOrderService(AbstractCancelOrderService):
    def cancel_order(self, order: Order) -> Order:
        order.cancel()
        # TODO: Cancel the order here
        return order
