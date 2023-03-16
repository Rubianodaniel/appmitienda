from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,"index.html")


def dashboard(request):
    return render(request,"components/dashboard.html")