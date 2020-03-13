from abc import ABC, abstractmethod


class Command(ABC):
    """Command Interface"""
    @abstractmethod
    def execute(self):
        raise NotImplementedError("You should implement this.")

    @abstractmethod
    def undo(self):
        raise NotImplementedError("You should implement this.")
