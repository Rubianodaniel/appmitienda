from django.urls import path
from app_main.views import (home,Users,dashboard,business,categories,products
                            ,new_sale,historical_sales,sales_report)


urlpatterns = [
    path('', home),
    path('dashboard/', dashboard, name='dashboard'),
    path('users/', Users.as_view(), name='users'),
    path('business/', business, name='business'),
    path('categories/', categories, name='categories'),
    path('products/',products, name="products"),
    path('newSale/',new_sale, name="new_sale"),
    path('historical_sales/',historical_sales, name="historical_sales"),
    path('sales_report/', sales_report, name= "sales_report"),
]   