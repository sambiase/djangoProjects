from django.shortcuts import render

def bootstrap_manual_site(request):
    return render(request=request,template_name='bootstrap_manual_website.html')
