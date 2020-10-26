from django.urls import path
from . import views

app_name = 'contact'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/timeline/', views.timeline_view, name='timeline'),
    path('create-post/', views.post_view, name='create_post'),

]
