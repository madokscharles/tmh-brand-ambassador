# competition/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('models/', views.models, name='models'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='competition/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='competition/logout.html'), name='logout'),
]