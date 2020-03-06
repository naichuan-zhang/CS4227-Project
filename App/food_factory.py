from abc import ABCMeta, abstractmethod

# https://www.hawli.cn/2018/04/03/%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F-02-%E6%8A%BD%E8%B1%A1%E5%B7%A5%E5%8E%82%E6%A8%A1%E5%BC%8F-Python%E5%AE%9E%E7%8E%B0/


class AbsFood:
    __metaclass__ = ABCMeta

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def price(self):
        pass


class AbsFoodFactory:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_food(self):
        pass

