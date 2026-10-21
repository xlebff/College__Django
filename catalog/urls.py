from django.urls import path
from . import views

urlpatterns = [
    path('', views.zone_list, name='zone_list'),
    path('zone/<int:pk>/', views.zone_detail, name='zone_detail'),
    path('zone/add/', views.zone_add, name='zone_add'),
    path('about/', views.about, name='about'),
]