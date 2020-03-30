from typing import Any


class Memento:
    """the memento"""

    def __init__(self, state: Any) -> None:
        self.__state = state

    def get_state(self) -> Any:
        """Originator uses this method when restoring its state"""
        return self.__state
