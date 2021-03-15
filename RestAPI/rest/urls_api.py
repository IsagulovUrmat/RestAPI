from django.urls import path
from .views import *

urlpatterns = [
    path('hard/', MealViewHard.as_view()),
    path('', MealView.as_view()),
    path('<int:meal_id>/', MealDetailView.as_view()),
]