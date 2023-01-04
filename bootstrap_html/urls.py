
from django.urls import path
from .views import bootstrap_template

urlpatterns = [
    path('bootstrap_template/', bootstrap_template)
]
