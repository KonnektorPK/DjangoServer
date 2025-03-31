from django.contrib import admin, auth
from django.urls import include, path

from django.shortcuts import render

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('map.urls')),
]