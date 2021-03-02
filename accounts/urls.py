from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(
        template_name="login.html"), name='login'),
<<<<<<< HEAD
=======
    path("adminlogin/", auth_views.LoginView.as_view(
        template_name="adminlogin.html"), name='adminlogin'),
>>>>>>> 86ccd745649ad54b3029d3a2f439bc01f885bcd7
    path("profile/", views.profile, name="profile"),
    path("logout/", auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("morang/", views.MorangView.as_view(), name="morang"),
    path("morang_detail/", views.MorangDetailView.as_view(), name="morang_detail"),
    path("contact/",views.contact,name='contact',)
]
