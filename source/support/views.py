from django.shortcuts import render

def support_page(request, *args, **kwargs):
    return render(request, 'support.html', {})

def community(request, *args, **kwargs):
    return render(request, 'community.html', {})
# Create your views here.
