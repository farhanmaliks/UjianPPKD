from django.urls import path
from .views import *

urlpatterns = [
    path('tes', tes, name='tes'),
]