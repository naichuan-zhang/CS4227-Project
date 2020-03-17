import pickle


class Memento:
    """
    the memento:
    store the current internal state
    restore the internal state to previous state
    """
    def __init__(self, state):
        self.__state = state

    def save_state(self):
        current_state = pickle.dumps(vars(self))
        return current_state

    def restore_state(self, memento):
        previous_state = pickle.loads(memento)
        vars(self).clear()
        vars(self).update(previous_state)

    def set_state(self, state):
        self.__state = state

    def get_state(self):
        return self.__state

    def __str__(self):
        return f'state: {self.__state}'
