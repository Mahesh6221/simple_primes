from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('primes/', output_page),
]