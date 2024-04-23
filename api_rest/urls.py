from django.contrib import admin
from django.urls import path , include

from . import views

urlpatterns = [
    path('', views.get_user, name='get_all_users'),
    path('user/<str:name>', views.get_user_by_name, name='get_user_by_name'),
    path('create/', views.create_user, name='create_user'),
    path('update/<str:name>', views.update_user, name='update_user'),
]
