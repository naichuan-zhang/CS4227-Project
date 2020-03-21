from order.factory.discount.abstractdiscount import AbstractDiscount


class GoldDiscount(AbstractDiscount):

    def get_discount(self):
        return 0.8
