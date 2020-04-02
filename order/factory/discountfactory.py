from enum import IntEnum

from order.factory.discount.golddiscount import GoldDiscount
from order.factory.discount.nodiscount import NoDiscount
from order.factory.discount.silverdiscount import SilverDiscount


class DiscountEnum(IntEnum):
    SILVER = 6
    GOLD = 11


class DiscountFactory:

    @staticmethod
    def create_discount(number_of_orders: int):
        if number_of_orders < DiscountEnum.SILVER:
            return NoDiscount()
        elif DiscountEnum.SILVER <= number_of_orders < DiscountEnum.GOLD:
            return SilverDiscount()
        elif number_of_orders >= DiscountEnum.GOLD:
            return GoldDiscount()
        else:
            return None
