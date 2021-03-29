from django.contrib import admin
from .models import Order, RestaurantProfile, Table, Promocode, MealToOrder

admin.site.register(Order)
admin.site.register(RestaurantProfile)
admin.site.register(Table)
admin.site.register(Promocode)
admin.site.register(MealToOrder)

