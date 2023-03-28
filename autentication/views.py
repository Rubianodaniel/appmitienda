from django.shortcuts import render, redirect
from app_main.models import Usuario
from .form import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username =  form.cleaned_data["username"]
            messages.success(request, f"usuario {username} ha sido creado")
            return redirect("/")
    else:
        form = UserRegisterForm()
    
    context = {"form":form}
    return render(request, "components/auth/register.html", context)


def login(request):
    context = {}
    return render(request, "components/auth/login.html", context)
