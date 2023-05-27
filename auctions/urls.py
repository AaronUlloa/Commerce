from django.urls import path

from . import views

app_name = "auctions"

urlpatterns = [
        path("", views.index, name="index"),
        path("login", views.login_view, name="login"),
        path("logout", views.logout_view, name="logout"),
        path("register", views.register, name="register"),        
        path("forget", views.forget, name="forget"),
        path("addNew", views.addNew, name="addNew")
    ]
