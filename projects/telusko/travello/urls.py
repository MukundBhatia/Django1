import os
from unicodedata import name
from django.urls import path

from telusko.settings import BASE_DIR

from . import views

urlpatterns = [
    path('', views.index, name='index'),

]
