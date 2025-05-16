from django.urls import path

from . import views

urlpatterns = [
    path("", views.scanqr, name="scanqr"),
]