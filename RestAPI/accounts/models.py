from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    phone = models.IntegerField(default=0)
    street = models.CharField(max_length=50)
    house = models.CharField(max_length=10)
    email = models.EmailField()
    bonuses = models.IntegerField(default=0, blank=True)
    order_count = models.PositiveIntegerField(default=0, blank=True)

    def __str__(self):
        return self.full_name

class Card(models.Model):

    balance = models.PositiveIntegerField(default=0)
    status = models.CharField(choices=(
        ('default', 'default'),
        ('non active', 'non active')
    ), max_length=20, default='non active')
    number = models.IntegerField(default=0)
    holder_name = models.CharField(max_length=50)
    date = models.DateField()
    code = models.IntegerField(default=0)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='cards')

    def __str__(self):
        return self.holder_name


