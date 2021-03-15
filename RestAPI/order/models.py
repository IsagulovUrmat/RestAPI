from django.db import models
from rest.models import Meal

class Order(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    table = models.PositiveIntegerField()
    status = models.CharField(choices=(
                                        ('Ready', 'Ready'),
                                        ('in_process', 'in_process')
                                    ), max_length=20, default='in_process')

    def __str__(self):
        return self.meal.name

