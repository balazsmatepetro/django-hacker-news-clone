from django.urls import path

from . import views

app_name = 'news'

urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit, name='submit'),
    path('<int:news_item_id>/comments/', views.comments, name='comments'),
]
