from django.urls import path
from .views import simple_html_withModels_function

urlpatterns = [
    path('simple_html_with_models/', simple_html_withModels_function)
]

