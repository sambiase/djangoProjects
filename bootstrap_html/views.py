from django.shortcuts import render

def bootstrap_template(request):
    return render(request,template_name='bootstrap_html_template.html')