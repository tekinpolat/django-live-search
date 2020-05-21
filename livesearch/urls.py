from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getdata/', views.getdata, name='getdata'),
]
