from django.urls import path
from .views import crypto_site

urlpatterns = [
    path('crypto_site/', crypto_site)
]
