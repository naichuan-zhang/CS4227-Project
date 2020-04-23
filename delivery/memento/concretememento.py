from delivery.memento.memento import Memento

class ConcreteMemento(Memento):

    def __init__(self, state: str) -> None:
        self.__state = state

    def get_state(self) -> str:
        return self.__state
