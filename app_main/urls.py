from django.urls import path
from app_main import views


urlpatterns = [
    path('', views.home),
    path('dashboard/', views.dashboard, name='dashboard'),
]