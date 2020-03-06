from abc import ABC, abstractmethod


class AbstractUserBuilder(ABC):
    """the builder interface"""
    @abstractmethod
    def set_username(self, username):
        raise NotImplementedError

    @abstractmethod
    def set_password(self, password):
        raise NotImplementedError

    @abstractmethod
    def set_email(self, email):
        raise NotImplementedError

    @abstractmethod
    def set_icon(self, icon):
        raise NotImplementedError

    @abstractmethod
    def save(self):
        raise NotImplementedError

    @abstractmethod
    def reset(self):
        raise NotImplementedError

    @abstractmethod
    def get_user(self):
        raise NotImplementedError
