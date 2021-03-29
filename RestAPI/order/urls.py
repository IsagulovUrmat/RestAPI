from django.urls import path
from .views import *

urlpatterns = [
    path('order/', OrderView.as_view()),
    path('table/', TableView.as_view()),
    path('table/<int:table_id>', TableDetailView.as_view()),
    path('profile/', RestaurantProfileView.as_view()),
    path('order/<int:order_id>/', ModifyOrderView.as_view())
]