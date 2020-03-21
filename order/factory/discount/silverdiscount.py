from order.factory.discount.abstractdiscount import AbstractDiscount


class SilverDiscount(AbstractDiscount):

    def get_discount(self):
        return 0.9
