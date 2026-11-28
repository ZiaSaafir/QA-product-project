from django.urls import path
from . import views

app_name = "retrieval"

urlpatterns = [
    path("", views.home, name="home"),
]
