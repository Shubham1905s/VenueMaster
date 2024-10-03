from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User     
from django.db import models
from .models import UploadFile
   
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ['title', 'file']
        
        
from django import forms
from .models import MVHallUploadFile

class MVHallUploadFileForm(forms.ModelForm):
    class Meta:
        model = MVHallUploadFile
        fields = ['title', 'file']
