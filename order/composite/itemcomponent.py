from abc import ABC, abstractmethod


class ItemComponent(ABC):
    """Composite Interface"""

    @abstractmethod
    def get_price(self):
        raise NotImplementedError("You should implement this.")

    # @abstractmethod
    # def get_name(self):
    #     raise NotImplementedError("You should implement this.")
