from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='HomePage'),

    path('location/<str:location_id>/', views.UserLocationRU, name='UserLocationRU'),
    path('en/location/<str:location_id>/', views.UserLocationEN, name='UserLocationEN'),
    path('location/', views.UserRU, name='UserRU'),
    path('en/location/', views.UserEN, name='UserEN'),

    path('create-error-report/', views.create_error_report, name='create_error_report'),
    path('search_location/', views.search_location, name='search_location'),
    path('getMapFromPoints/', views.getMapFromPoints, name='getMapFromPoints'),
]