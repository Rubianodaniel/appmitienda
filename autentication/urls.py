from  django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('register/', views.register, name="register"),
    path("accounts/login/", LoginView.as_view(template_name = "components/auth/login.html"), name="login"),
    path("logout", LogoutView.as_view(template_name = "components/auth/logout.html"), name="logout"),


]