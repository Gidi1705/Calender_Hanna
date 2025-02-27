from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_day, name='index'),
    path('day/<str:date_str>/', views.get_day, name='get_day'),
    path('overview/', views.overview, name='overview'),
]
