from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Route de base pour /users/
    path('register/', views.register),
    path('login/', views.login_view),
]
