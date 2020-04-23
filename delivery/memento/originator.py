from __future__ import annotations

from delivery.memento.concretememento import ConcreteMemento
from delivery.memento.memento import Memento


class Originator():

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Delivery state is: {self._state}")

    def set_state(self, state: str) -> None:
        self._state = state

    def save(self) -> Memento:
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:
        self._state = memento.get_state()
        print(f"Delivery has changed to: {self._state}")