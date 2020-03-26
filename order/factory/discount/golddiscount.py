from decimal import Decimal

from order.factory.discount.abstractdiscount import AbstractDiscount


class GoldDiscount(AbstractDiscount):

    def get_multiplier(self):
        return Decimal('0.8')
