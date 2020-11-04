from django.urls import path
from . import views

app_name = 'bookinglist'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/bookinglist/', views.home_view, name='home'),
]
