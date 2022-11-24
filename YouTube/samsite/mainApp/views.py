from django.shortcuts import render
from django.http import HttpResponse


def index(response):
    return HttpResponse('<h1> This is the Main Page </h1>')


def sub_page(response):
    return HttpResponse('<h1> This is the Sub Page </h1>')
