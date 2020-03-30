from order.memento.memento import Memento
from order.memento.originator import Originator


class Caretaker:
    """
    the caretaker:
    sees narrow interface to the memento - can only pass the memento to the other objects
    """

    def __init__(self, originator: Originator) -> None:
        """caretaker can request a memento from originator"""
        self.__mementos = []
        self.__originator = originator

    def save(self) -> None:
        """save state to memento and add to list"""
        self.__mementos.append(
            self.__originator.save_memento())

    def undo(self) -> None:
        """revert back to the previous state from list"""
        if not len(self.__mementos):
            return
        memento = self.__mementos.pop()
        try:
            self.__originator.restore_memento(memento)
        except Exception as e:
            print(e)
