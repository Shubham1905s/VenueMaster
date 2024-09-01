from django.urls import path
from .views import *

app_name="myapp"

urlpatterns = [
    path("",home,name="home"),
    path("audi/",audi,name="audi"),
    path("success/",success,name="success"),
    path("errbook/",errorbook,name="errbook"),
    path("registerPage/",registerPage,name="registerPage"),
    path("loginPage/",loginPage,name="loginPage"),
    path("logout/",logoutUser,name="logoutUser")
]



