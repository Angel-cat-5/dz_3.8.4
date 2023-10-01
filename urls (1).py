from django.urls import path
from .views import rp

urlpatterns = [
    path('', rp),
]