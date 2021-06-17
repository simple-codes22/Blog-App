from django.urls import path
from .views import support_page
app_name = "support"

urlpatterns = [
    path('base/', support_page, name="main")
]