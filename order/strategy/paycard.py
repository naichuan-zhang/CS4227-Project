from order.strategy.strategy import Strategy
from order.models import PayCard


class PayCard(Strategy):

    def payMethod(self, name, number):
        self.__payment = PayCard(name=name, number=number)
        self.__payment.save()