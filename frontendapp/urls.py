from django.urls import path
from .views import *



urlpatterns=[
    path('sample/',sample),
    path('home/',home)


]