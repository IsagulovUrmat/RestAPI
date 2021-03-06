from django.db import models
from rest.models import Meal
from accounts.models import UserProfile


class Comment(models.Model):

    text = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    meal = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
