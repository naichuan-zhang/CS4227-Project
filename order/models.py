from django.db import models

from user.models import User


class Order(models.Model):
    pay_method_choices = (
        (1, 'Credit Card'),
        (2, 'AliPay'),
        (3, 'WeChat')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pay_method = models.SmallIntegerField(choices=pay_method_choices, default=1)
    date = models.DateField()

    class Meta:
        db_table = 'order'
