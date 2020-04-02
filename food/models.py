from enum import IntEnum

from django.db import models


class FoodTypeEnum(IntEnum):
    STARTER = 0
    MAIN = 1
    DESSERT = 2
    DRINK = 3

    @classmethod
    def tuples(cls):
        return tuple((state.name, state.value) for state in cls)


class FoodType(models.Model):
    """food type model"""

    class Meta:
        db_table = 'food_type'

    def __str__(self):
        return self.name


class Food(models.Model):
    """food model"""
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'food'

    def __str__(self):
        return self.name


class FoodFoodType(models.Model):
    """connect food and food type models"""
    status_choices = (
        (0, 'unavailable'),
        (1, 'available'),
    )
    type = models.ForeignKey(to='FoodType', on_delete=models.CASCADE)
    food = models.ForeignKey(to='Food', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.SmallIntegerField(default=1, choices=status_choices)

    class Meta:
        db_table = 'food_food_type'
