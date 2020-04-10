from order.strategy.strategy import Strategy


class Context():

    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        self._strategy = strategy

    def pay(self, par1, par2):
        self._strategy.payMethod(par1, par2)

