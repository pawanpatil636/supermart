from django.urls import path
from .import views

app_name="account"
urlpatterns =[
    path("register/" , views.register, name="register"),
    path("login/" , views.logins, name="login"),
    path("logout/" , views.logout_view, name="logout"),
    path("account/<int:pk>/" , views.account_view, name="account"),

]