from typing import Any

from order.memento.memento import Memento


class Originator:
    """
    the originator:
    sees wide interface - can access all the data necessary to restore itself to its previous state
    """

    def __init__(self, state: Any) -> None:
        self.__state = state

    def save_memento(self) -> Memento:
        """save the current state inside a memento"""
        return Memento(self.__state)

    def restore_memento(self, memento: Memento) -> None:
        """restore the Originator's state from a memento"""
        self.__state = memento.get_state()

    def set_state(self, state: Any) -> None:
        """set state"""
        self.__state = state

    def get_state(self) -> Any:
        """get state"""
        return self.__state
