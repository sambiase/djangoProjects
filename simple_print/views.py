from django.shortcuts import render
from django.http import HttpResponse


def simple_print(request):
    return HttpResponse('<h1> This is a simple print </h1>')
