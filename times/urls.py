from django.urls import path
from .views import times

urlpatterns = [
    path('index/',times)
]
