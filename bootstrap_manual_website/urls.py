from django.urls import path
from .views import bootstrap_manual_site


urlpatterns = [
    path('manual_bootstrap/', bootstrap_manual_site)
]
