from django.contrib.auth.models import User
from django.db import models
from rest.models import Meal
from accounts.models import UserProfile


class Table(models.Model):

    areas = (
        ('Main Hall', 'Main Hall'),
        ('Outdoor', 'Outdoor'),
        ('VIP', 'VIP')
    )

    statuses = (
        ('Reserved', 'Reserved'),
        ('Empty', 'Empty')
    )

    area = models.CharField(choices=areas, max_length=20, default='Main Hall')
    status = models.CharField(choices=statuses, max_length=20, default='Empty')

    def __str__(self):
        return self.area



class RestaurantProfile(models.Model):

    full_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=0)
    date_start = models.DateField(auto_now_add=True)
    date_end = models.DateField()
    salary = models.PositiveIntegerField(default=0)
    schedule = models.CharField(choices=(
        ('2/2', '2/2'),
        ('5/2', '5/2')
    ), max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class Order(models.Model):
    total_price = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(choices=(
                                        ('Ready', 'Ready'),
                                        ('in_process', 'in_process'),
                                        ('closed', 'closed')
                                    ), max_length=20, default='in_process')
    userprofile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    worker = models.ForeignKey(RestaurantProfile, on_delete=models.SET_NULL, null=True, blank=True)

    payment_type = models.CharField(choices=(
        ('card', 'card'),
        ('cash', 'cash')
    ), max_length=5, default='cash')
    promocode = models.CharField(max_length=10, blank=True, null=True, default='1')





class Promocode(models.Model):

    code = models.CharField(max_length=10, unique=True)
    sale = models.FloatField(default=0.1)
    end_date = models.DateField()
    status = models.CharField(choices=(
        ('active', 'active'),
        ('dead', 'dead')
    ), max_length=10, default='active')

    def __str__(self):
        return f'{self.code},{self.status}'


class MealToOrder(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='MTO')
    quantity = models.PositiveIntegerField(default=1)






