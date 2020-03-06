from abc import ABCMeta, abstractmethod, ABC

from App.models import User


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
    def get_user():
        """return the user"""
        pass


class UserBuilder(IUserBuilder, ABC):
    """the concrete builder"""
    def __init__(self):
        self.user = User()

    def set_username(self, value):
        self.user.username = value
        return self

    def set_password(self, value):
        self.user.password = value
        return self

    def set_email(self, value):
        self.user.email = value
        return self

    def set_icon(self, value):
        self.user.icon = value
        return self

    def save(self):
        """save user to database"""
        self.user.save()
        return self

    def get_user(self):
        return self.user


# the user for registration
class GeneralUser:
    """the director, building a different representation"""
    @staticmethod
    def construct(username, password, email, icon):
        return UserBuilder() \
            .set_username(username) \
            .set_password(password) \
            .set_email(email)\
            .set_icon(icon)\
            .save()\
            .get_user()


class GeneralUserWithoutIcon:
    """the director, building a different representation"""
    @staticmethod
    def construct(username, password, email):
        return UserBuilder()\
            .set_username(username)\
            .set_password(password)\
            .set_email(email)\
            .save()\
            .get_user()
