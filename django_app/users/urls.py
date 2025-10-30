from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view, add_offer


urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
    path("register/", register_view, name="register"),
    path("add_offer/", add_offer, name="add_offer"),
]
