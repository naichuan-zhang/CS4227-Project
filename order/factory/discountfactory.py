from order.factory.discount.golddiscount import GoldDiscount
from order.factory.discount.nodiscount import NoDiscount
from order.factory.discount.silverdiscount import SilverDiscount


class DiscountFactory:

    @staticmethod
    def create_discount(amount: int):
        if amount <= 5:
            return NoDiscount()
        elif 5 < amount <= 10:
            return SilverDiscount()
        elif amount > 10:
            return GoldDiscount()
        else:
            return None
