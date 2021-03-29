from django.db import models
from order.models import RestaurantProfile
from accounts.models import UserProfile

class Rate(models.Model):

    worker = models.ForeignKey(RestaurantProfile, on_delete=models.SET_NULL, null=True)
    star = models.PositiveIntegerField(default=None, null=True)
    date_created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)



