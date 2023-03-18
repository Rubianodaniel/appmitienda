from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import Usuario


def home(request):
    return render(request,"index.html")


def dashboard(request):
    return render(request,"components/dashboard/dashboard.html")


class Users(View):
    def get(self, request):
        lst_user = Usuario.objects.all()
        
        context = {
            "lst_user": lst_user
        }

        return render(request, "components/administration/users.html",context)


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