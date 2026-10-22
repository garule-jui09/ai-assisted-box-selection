from django.urls import path
from . import views

app_name = "box_selector"

urlpatterns = [
    path("", views.home, name="home"),
]