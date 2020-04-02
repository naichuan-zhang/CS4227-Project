from order.models import Order, Cart, Item, OrderItem
from order.visitor.abstractvisitor import AbstractVisitor
from order.visitor.visitable import Visitable


class StringVisitor(AbstractVisitor):
    def __init__(self) -> None:
        super().__init__()

    def visit(self, element: Visitable):
        super().visit(element)

    def _visit_order(self, element: Order):
        string = "Order ID: " + str(element.id) + " / "
        string += "User ID: " + str(element.user.id) + " / "
        string += "Total Price:  " + str(element.total_price) + " / "
        string += "Timestamp: " + str(element.timestamp) + " / "
        string += "State: " + str(element.state)
        return string

    def _visit_cart(self, element: Cart):
        string = "Cart ID: " + str(element.id) + " / "
        string += "User ID: " + str(element.user.id) + " / "
        string += "Item ID:  " + str(element.item.id) + " / "
        string += "Quantity: " + str(element.num)
        return string

    def _visit_item(self, element: Item):
        string = "Item ID: " + str(element.id) + " / "
        string += "Name: " + str(element.name) + " / "
        string += "Type:  " + str(element.type) + " / "
        string += "Price: " + str(element.price) + " / "
        string += "Stock: " + str(element.stock)
        return string

    def _visit_order_item(self, element: OrderItem):
        string = "OrderItem ID: " + str(element.id) + " / "
        string += "Item ID:  " + str(element.item.id) + " / "
        string += "Order ID:  " + str(element.order.id) + " / "
        string += "Quantity: " + str(element.amount)
        return string
