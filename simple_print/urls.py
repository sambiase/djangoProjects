from django.urls import path
from .views import simple_print

urlpatterns = [
    path('simple_print/', simple_print)
]
