from order.command.commandmanager import CommandManager
from order.command.ordercommand import OrderCommand
from order.command.orderservices import OrderOrderService, CancelOrderService
from order.models import Order
from user.models import User


class OrderFramework:
    def __init__(self):
        self.__order_command = None
        self.__command_manager = CommandManager()
        self.__create_order_service = OrderOrderService()
        self.__cancel_order_service = CancelOrderService()

    def create_order(self, user_id: int, total_price: float) -> Order:
        user = User.objects.get(id=user_id)
        order = Order(user=user, total_price=total_price)
        return self.__command_manager.execute(
            OrderCommand.order_service(self.__create_order_service, order))
        # return self.__order_command.set_order(order)\
        #     .order_service(self.__create_order_service).execute()

    def cancel_order(self, order_id: id) -> Order:
        order = Order.objects.get(id=order_id)
        return self.__command_manager.execute(
            OrderCommand.order_service(self.__cancel_order_service, order))
        # return self.__order_command.set_order(order)\
        #     .order_service(self.__cancel_order_service).execute()

    def undo(self, times: int = 1):
        self.__command_manager.undo(times=times)
