from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def payMethod(self):
        pass