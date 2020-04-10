from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def payMethod(self, par1, par2):
        pass