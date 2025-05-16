from django.urls import path

from . import views

urlpatterns = [
    path("/generar", views.index, name="index"),
]