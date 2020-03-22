from abc import ABC, abstractmethod

from order.models import Order


class AbstractOrderOrderService(ABC):
    @abstractmethod
    def create_order(self, order: Order) -> Order:
        raise NotImplementedError("You have to implement this")

    @abstractmethod
    def undo(self, order: Order):
        raise NotImplementedError("You have to implement this")


class OrderOrderService(AbstractOrderOrderService):
    def create_order(self, order: Order) -> Order:
        # set the order to state ORDERED
        order.order()
        # save the order to database
        order.save()
        return order

    def undo(self, order: Order):
        order.cancel()
        order.save()


class AbstractCancelOrderService(ABC):
    @abstractmethod
    def cancel_order(self, order: Order) -> Order:
        raise NotImplementedError("You have to implement this")

    @abstractmethod
    def undo(self, order: Order):
        raise NotImplementedError("You have to implement this")


class CancelOrderService(AbstractCancelOrderService):
    def cancel_order(self, order: Order) -> Order:
        # set the order to state CANCELLED
        order.cancel()
        # save the order to database
        order.save()
        return order

    def undo(self, order: Order):
        order.order()
        order.save()
