from django.urls import path
from app_main import views


urlpatterns = [
    path('', views.home),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('users/', views.users, name='users'),
    path('business/', views.business, name='business'),
    path('categories/', views.categories, name='categories'),
    path('products/',views.products, name="products"),
    path('newSale/',views.new_sale, name="new_sale"),
    path('historical_sales/',views.historical_sales, name="historical_sales"),
    path('sales_report/', views.sales_report, name= "sales_report"),
]   