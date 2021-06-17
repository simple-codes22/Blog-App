from django.shortcuts import render, redirect
from .models import User, Publisher, Post
from django.urls import reverse

def main(request, *args, **kwargs):
    content = {'posts': Post.objects.all()}
    return render(request, 'main.html', content)

def dash(request, id, user_name, *args, **kwargs):
    user = User.objects.get(id=id, username=user_name)
    return render(request, "dashboard.html", {'user': user})

def sign_up(request, *args, **kwargs):
    if request.method == "POST":
        user = User.objects.get(first_name=request.POST.get(username=request.POST.get('u-name')), e_mail=request.POST.get('e-mail'))
        return redirect(reverse('main:dash', kwargs={'id': user.id, 'user_name': user.username}))
    return render(request, 'signup.html', {})

def login(request, *args, **kwargs):
    if request.method == "POST":
        user = User.objects.get(e_mail=request.POST.get('e-mail'), username=request.POST.get('u-name'))
        return redirect(reverse('main:dash', kwargs={'id': user.id, 'user_name': user.username}))
    return render(request, 'login.html', {})

def add_post(request, *args, **kwargs):
    if request.method == "POST":
        return redirect('/')
    return render(request, 'edit.html', {})

def view(request, *args, **kwargs):
    return render(request, 'viewpost.html', {})
# Create your views here.
