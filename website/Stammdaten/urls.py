from django.urls import path
from . import views

app_name = 'Stammdaten'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/Stammdaten', views.index, name='Stammdaten'),
]
