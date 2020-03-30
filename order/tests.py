from django.test import TestCase

from order.memento.caretaker import Caretaker
from order.memento.originator import Originator
from order.orderframework import OrderFramework
from user.models import User


__author__ = 'naichuan'


class MementoTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        """set init state"""
        cls.state = 'state 1'

    def test_memento(self) -> None:
        originator = Originator(state=self.state)
        caretaker = Caretaker(originator=originator)
        caretaker.save()
        self.assertEqual(originator.get_state(), 'state 1')
        originator.set_state('state 2')
        caretaker.save()
        self.assertEqual(originator.get_state(), 'state 2')
        # roll back to original state
        caretaker.undo()
        caretaker.undo()
        print(originator.get_state())
        self.assertEqual(originator.get_state(), 'state 1')


class OrderFrameworkTestCase(TestCase):
    """test case for order framework with Command DP"""

    @classmethod
    def setUpTestData(cls):
        """create an order"""
        cls.framework = OrderFramework()
        cls.user = User.objects.create(username='username',
                                       password='password',
                                       email='email',
                                       icon=None, is_active=True)
        cls.order = cls.framework\
            .create_order(user_id=cls.user.id,
                          total_price=100)

    def test_order_framework_with_command_dp(self):
        user = User.objects.get(username='username')
        self.assertEqual(self.order.user, user)
        self.assertEqual(self.order.total_price, 100)
