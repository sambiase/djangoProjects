from django.urls import path
from .views import bootstrap_manual_site


urlpatterns = [
    path('bootstrap_manual_page/', bootstrap_manual_site)
]
