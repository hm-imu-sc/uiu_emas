from django.urls import path
from . import views

app_name = "app_general"

urlpatterns = [
    path("index/", views.Index.as_view(), name="index"),
]