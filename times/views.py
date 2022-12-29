from django.shortcuts import render
from .models import Times

def times(request):
    list_times = Times
    context = {
        'times': list_times
    }
    return render(request,'index.html',context)

