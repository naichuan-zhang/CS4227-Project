from decimal import Decimal

from order.factory.discount.abstractdiscount import AbstractDiscount


class NoDiscount(AbstractDiscount):

    def get_discount(self):
        return Decimal('1.0')
