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