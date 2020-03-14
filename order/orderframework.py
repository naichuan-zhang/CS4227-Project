from order.command.ordercommand import OrderCommand
from order.command.orderservices import OrderOrderService, CancelOrderService
from order.models import Order
from user.models import User


class OrderFramework:
    def __init__(self):
        self.__order_command = None
        self.__create_order_service = OrderOrderService()
        self.__cancel_order_service = CancelOrderService()

    def create_order(self, order_id: int, user_id: int) -> Order:
        # TODO: Might use a creational design pattern here ???
        user = User.objects.get(id=user_id)
        order = Order(id=order_id, user=user)
        return self.__order_command.set_order(order)\
            .order_service(self.__create_order_service).execute()

    def cancel_order(self, order_id: id) -> Order:
        order = Order.objects.get(id=order_id)
        return self.__order_command.set_order(order)\
            .order_service(self.__cancel_order_service).execute()
