from django.urls import path

from . import views

app_name = 'news'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:news_item_id>/comments/', views.comments, name='comments'),
]
