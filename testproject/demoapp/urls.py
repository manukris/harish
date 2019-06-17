from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index1, name='index'),
    path ('form/', views.oneform, name='index1'),
    path ('tempview/', views.Dataview.as_view(), name='tempview'),
    path ('listview/', views.OneListView.as_view(), name='listview'),
    path('createview/', views.OneCreate.as_view(), name='listcreate'),

]
