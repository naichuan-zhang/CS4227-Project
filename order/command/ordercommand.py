from order.command.command import Command
from order.command.orderservices import AbstractOrderOrderService, AbstractCancelOrderService
from order.command.undoable import Undoable
from order.models import Order


class OrderCommand(Command, Undoable):
    """
    the concrete command

    set_order -> order_service -> execute/undo
    """

    def __init__(self):
        self.__order = None

    def set_order(self, order):
        self.__order = order

    @classmethod
    def order_service(cls, service) -> 'OrderCommand':
        if isinstance(service, AbstractOrderOrderService):
            return cls._create_order(service)
        elif isinstance(service, AbstractCancelOrderService):
            return cls._cancel_order(service)

    @classmethod
    def _create_order(cls, service: AbstractOrderOrderService) -> 'OrderCommand':
        # TODO Not Done yet
        pass

    @classmethod
    def _cancel_order(cls, service: AbstractCancelOrderService) -> 'OrderCommand':
        # TODO Not Done yet
        pass

    def execute(self):
        """order"""
        # TODO Not Done yet

    def undo(self):
        """cancel the order"""
        # TODO Not Done yet


# class OrderOrderCommand(Command, Undoable):
#     """concrete command for ordering an order"""
#
#     def __init__(self, order: Order):
#         self.__order = order
#
#     def execute(self):
#         self.__order.order()
#
#     def undo(self):
#         self.__order.cancel()
#
#
# class CancelOrderCommand(Command, Undoable):
#     """concrete command for cancelling an order"""
#
#     def __init__(self, order: Order):
#         self.__order = order
#
#     def execute(self):
#         self.__order.cancel()
#
#     def undo(self):
#         self.__order.order()

