from abc import ABC, abstractmethod


class AbstractDiscount(ABC):
    """Discount Interface"""

    @abstractmethod
    def get_discount(self):
        raise NotImplementedError("You should implement this.")
