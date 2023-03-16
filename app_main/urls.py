from django.urls import path
from app_main import views


urlpatterns = [
    path('', views.home),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('users/', views.users, name='users'),
    path('business/', views.business, name='business'),
    path('categories/', views.categories, name='categories'),
    path('products/',views.products, name="products")

]