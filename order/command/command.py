from abc import abstractmethod, ABCMeta


class Command(metaclass=ABCMeta):
    """Command Interface"""

    @abstractmethod
    def execute(self):
        raise NotImplementedError("You should implement this.")
