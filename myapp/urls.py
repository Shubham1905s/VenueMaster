from django.urls import path
from .views import *

app_name="myapp"

urlpatterns = [
    path("",home,name="home"),
    path("audi",audi,name="audi"),
    path("success",success,name="success"),
]



