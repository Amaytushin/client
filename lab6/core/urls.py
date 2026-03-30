from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list_view, name='post_list'),
    path('create/', views.create_post, name='create_post'), # Шинэ зам
]