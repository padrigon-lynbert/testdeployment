from django.contrib import admin
from django.urls import path
from .views import render_app

urlpatterns = [
    path('', render_app, name='render_app'),
]
