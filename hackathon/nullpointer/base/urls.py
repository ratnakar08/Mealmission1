from django.contrib import admin
from django.urls import path,include
from . import views as v
app_name='base'
urlpatterns = [
   path('',v.home,name='home')
]
