from django.test import TestCase

from user.models import User
from user.userbuilder.userbuilder import UserBuilder
from user.userbuilder.userdirector import UserDirector


__author__ = 'naichuan'


class UserBuilderTestCase(TestCase):

    def setUp(self) -> None:
        user_director = UserDirector(UserBuilder())
        user1 = user_director.construct(username='user1',
                                        password='password1',
                                        email='test@gmail.com',
                                        icon=None)
        user2 = user_director.construct(username='user2',
                                        password='password2',
                                        email='test@163.com',
                                        icon=None)
        print("username of user1: ", user1)
        print("username of user2: ", user2)

    def test_builder(self) -> None:
        user = User.objects.get(username='user1')
        self.assertEqual(user.email, 'test@gmail.com')
        user2 = User.objects.get(email__contains='@163.com')
        self.assertEqual(user2.username, 'user2')
