from decimal import Decimal

from order.factory.discount.abstractdiscount import AbstractDiscount


class GoldDiscount(AbstractDiscount):

    def get_discount(self):
        return Decimal('0.8')
