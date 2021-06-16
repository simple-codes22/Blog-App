from django.shortcuts import render, redirect
from .models import User, Publisher, Post

def main(request, *args, **kwargs):
    content = {'posts': Post.objects.all()}
    return render(request, 'main.html', content)

def sign_up(request="GET", *args, **kwargs):
    if request.method == "POST":
        return redirect('/')
    return render(request, 'signup.html', {})

def login(request, *args, **kwargs):
    if request.method == "POST":
        return redirect('/')
    return render(request, 'login.html', {})

def add_post(request, *args, **kwargs):
    if request.method == "POST":
        return redirect('/')
    return render(request, 'edit.html', {})
# Create your views here.
