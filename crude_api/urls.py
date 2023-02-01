from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('parsedata', views.parse_data, name='parse-data'),
    path('', views.home, name='home'),

]
