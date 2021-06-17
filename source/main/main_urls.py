from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    path('', main, name="index"),
    path('new/', sign_up, name="sign-up"),
    path('login/', login, name="login"),
    path('post/', view, name="view-post"),
    path('dash/<int:id>/<str:user_name>/', dash, name="dash")
]