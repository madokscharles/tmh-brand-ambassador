# models_app/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('competitions/', views.competition_list, name='competition_list'),
    path('competitions/<int:competition_id>/', views.competition_detail, name='competition_detail'),
    path('competitions/<int:competition_id>/new_entry/', views.create_entry, name='create_entry'),
    path('profile/update/', views.profile_update, name='profile_update'),
]