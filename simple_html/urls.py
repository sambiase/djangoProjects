from django.urls import path
from .views import simple_html_function

urlpatterns = [
    path('simple_html/',simple_html_function)
]
