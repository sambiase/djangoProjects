from django.shortcuts import render

def simple_html_function(request):
    return render(request, 'simple_html.html')
