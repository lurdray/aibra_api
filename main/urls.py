from django.urls import path
from . import views

app_name = "main"

from . import views
from rest_framework import routers
from django.urls import path, include


urlpatterns = [

    #
    path('get-address/<str:name>/', views.GetAddress),
    path('get-name/<str:address>/', views.GetName),
    
    ]