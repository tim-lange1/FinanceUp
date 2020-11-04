from django.urls import path
from . import views

app_name = 'Stammdaten'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/Stammdaten/', views.home_view, name='home'),
]
