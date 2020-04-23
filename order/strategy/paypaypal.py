from order.strategy.strategy import Strategy
from order.models import PayPal


class PayPaypal(Strategy):

    def payMethod(self, email, password):
        self._payment = PayPal(email=email, password=password)
        self._payment.save()