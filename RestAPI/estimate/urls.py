from django.urls import path
from .views import *

urlpatterns = [
    path('estimate/', RateView.as_view()),
    path('estimate/<int:worker_id>/', RateWorkerView.as_view())
]