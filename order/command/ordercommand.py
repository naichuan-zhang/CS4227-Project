from typing import Callable, List, Tuple

from order.command.command import Command
from order.command.orderservices import AbstractOrderOrderService, AbstractCancelOrderService
from order.command.undoable import Undoable
from order.models import Order

ExecFunc = Callable[[Order], Order]
UndoFunc = Callable[[Order], None]


class OrderCommand(Command, Undoable):
    """the concrete command"""

    def __init__(self, order: Order, execute: ExecFunc, undo: UndoFunc):
        self.__order = order
        self.__execute = execute
        self.__undo = undo
        self.__orders: List[Order] = list()

    @classmethod
    def order_service(cls, service, order) -> 'OrderCommand':
        if isinstance(service, AbstractOrderOrderService):
            return cls._for_create_order(service, order)
        elif isinstance(service, AbstractCancelOrderService):
            return cls._for_cancel_order(service, order)
        else:
            raise NotImplementedError("No available service type found!")

    @classmethod
    def _for_create_order(cls, service: AbstractOrderOrderService, order: Order) -> 'OrderCommand':
        exec_func: ExecFunc = lambda o: service.create_order(o)
        undo_func: UndoFunc = lambda o: order.delete()
        return cls(order, exec_func, undo_func)

    @classmethod
    def _for_cancel_order(cls, service: AbstractCancelOrderService, order: Order) -> 'OrderCommand':
        exec_func: ExecFunc = lambda o: service.cancel_order(o)
        # TODO: Undo -> Need to be implemented here
        undo_func: UndoFunc = lambda o: None
        return cls(order, exec_func, undo_func)

    def execute(self) -> Order:
        order: Order = self.__execute(self.__order)
        self.__orders.append(order)
        return order

    def undo(self):
        order = self.__orders.pop()
        self.__undo(order)

    def __len__(self):
        return len(self.__orders)


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

