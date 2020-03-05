import abc


class AbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_user(self):
        pass
