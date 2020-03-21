from order.factory.discount.abstractdiscount import AbstractDiscount


class NoDiscount(AbstractDiscount):

    def get_discount(self):
        return 1
