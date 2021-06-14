from django.urls import path
from .views import *
app_name = "main"

urlpatterns = [
    path('', main, name="index"),
    path('new/', sign_up, name="sign-up"),
]