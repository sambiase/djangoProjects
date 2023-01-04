from django.shortcuts import render
from .models import Countries


def simple_html_withModels_function (request):
    countries = Countries.objects.all()
    context = {
        'countries':countries
    }
    return render (request, 'simple_html_withModels.html',context)