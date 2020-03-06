from abc import ABCMeta, abstractmethod, ABC

from App.logger import logger
from App.models import User

# TODO: FIX THIS !!!!!!!!!!!!
# Builder Design Pattern
class IUserBuilder(metaclass=ABCMeta):
    """the builder interface"""
    @staticmethod
    @abstractmethod
    def set_username(value):
        """set username"""
        pass

    @staticmethod
    @abstractmethod
    def set_password(value):
        """set password"""
        pass

    @staticmethod
    @abstractmethod
    def set_email(value):
        """set email address"""
        pass

    @staticmethod
    @abstractmethod
    def set_icon(value):
        """set icon"""
        pass

    @staticmethod
    @abstractmethod
    def save():
        """save user to database"""
        pass

    @staticmethod
    @abstractmethod
    def reset():
        """reset user"""
        pass

    @staticmethod
    @abstractmethod
    def get_user():
        """return the user"""
        pass


class UserBuilder(IUserBuilder, ABC):
    """the concrete builder"""
    def __init__(self):
        super().__init__()
        self.__user = User()

    @logger
    def set_username(self, value):
        self.__user.username = value
        return self

    @logger
    def set_password(self, value):
        self.__user.password = value
        return self

    @logger
    def set_email(self, value):
        self.__user.email = value
        return self

    @logger
    def set_icon(self, value):
        self.__user.icon = value
        return self

    @logger
    def save(self):
        self.__user.save()
        return self

    @logger
    def reset(self):
        self.__user = User()

    @logger
    def get_user(self):
        return self.__user


# the user for registration
class GeneralUser:
    """the director, building a different representation"""
    def __init__(self, builder):
        super().__init__()
        self.__builder = builder

    @logger
    def construct(self, username, password, email, icon):
        return self.__builder.reset() \
            .set_username(username) \
            .set_password(password) \
            .set_email(email)\
            .set_icon(icon)\
            .save()\
            .get_user()


class GeneralUserWithoutIcon:
    """the director, building a different representation"""
    def __init__(self, builder: IUserBuilder):
        super().__init__()
        self.__builder = builder

    @logger
    def construct(self, username, password, email):
        return self.__builder.reset()\
            .set_username(username)\
            .set_password(password)\
            .set_email(email)\
            .save()\
            .get_user()
