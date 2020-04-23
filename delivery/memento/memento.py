from abc import ABC, abstractmethod


class Memento(ABC):

    @abstractmethod
    def get_state(self) -> str:
        pass