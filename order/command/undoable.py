from abc import ABCMeta, abstractmethod


class Undoable(metaclass=ABCMeta):
    """the interface for defining undoable operation"""

    @abstractmethod
    def undo(self):
        raise NotImplementedError("You should implement this.")
