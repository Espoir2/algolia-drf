from django.urls import path

# Internals
from . import views

urlpatterns = [
    path('', views.api_home)
]
