from django.conf.urls import include, url
from django.contrib import admin
from api import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'process', views.process),
]
