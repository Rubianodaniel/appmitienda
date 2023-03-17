from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,"index.html")


def dashboard(request):
    return render(request,"components/dashboard/dashboard.html")


def users(request):
    return render(request, "components/administration/users.html")


def business(request):
    return render(request, "components/administration/business.html")

def categories(request):
    return render(request, "components/inventory/categories.html")

def products(request):
    return render(request, "components/inventory/products.html")

def new_sale(request):
    return render(request, "components/sales/new_sale.html")

def historical_sales(request):
    return render(request, "components/sales/historical_sales.html")

def sales_report(request):
    return render(request, "components/report_sales/report_sales.html")