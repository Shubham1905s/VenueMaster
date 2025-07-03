from django.urls import include, path
from .views import *
from .views import authView, home
app_name="myapp"

urlpatterns = [
    path("",home,name="home"),
    path("audi/",audi,name="audi"),
    path("success/",success,name="success"),
    path("errbook/",errorbook,name="errbook"),
    path("registerPage/",registerPage,name="registerPage"),
    path("loginPage/",loginPage,name="loginPage"),
    path("logout/",logoutUser,name="logoutUser"),
    path("MVhall/",MVhall,name="MVhall"),
    path("registererror",registererror,name="registererror"),
    path("regMVhall/",MVhall,name="regMVhall"),
    # path("loginPageMVhall/",loginPageMVhall,name="loginPageMVhall"),
    path("upload_file/",upload_file,name ="upload_file"),
    path("upload_mvhall_file",upload_mvhall_file,name="upload_mvhall_file"),
    path("signup/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
    ]



