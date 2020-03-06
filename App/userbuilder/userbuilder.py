from abc import ABC

from App.models import User
from App.userbuilder.abstractuserbuilder import AbstractUserBuilder


class UserBuilder(AbstractUserBuilder, ABC):
    """the concrete builder"""
    def __init__(self):
        super(UserBuilder, self).__init__()
        self.__user = User()

    def set_username(self, username):
        self.__user.username = username
        return self

    def set_password(self, password):
        self.__user.password = password
        return self

    def set_email(self, email):
        self.__user.email = email
        return self

    def set_icon(self, icon):
        self.__user.icon = icon
        return self

    def save(self):
        self.__user.save()
        return self

    def reset(self):
        self.__user = User()
        return self

    def get_user(self):
        return self.__user
