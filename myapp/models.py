from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from .managers import CustomUserManager




class Booking(models.Model):
    club_name = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.club_name} - {self.date} ({self.start_time} to {self.end_time})"


class MVHallBooking(models.Model):
    club_name = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.club_name} - {self.date} ({self.start_time} to {self.end_time})"

#Django admin interface to manage and input information about the Auditorium that will then be displayed on the audi         
class AuditoriumInfo(models.Model):
    description = models.TextField()
    capacity = models.IntegerField()
    facilities = models.TextField()
    def __str__(self):
        return f"Auditorium Information"
    
    
class MVHallInfo(models.Model):
    description = models.TextField()
    capacity = models.IntegerField()
    facilities = models.TextField()

    def __str__(self):
        return f"MV Hall Information"
    
    
class AuditoriumFiles(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField()

    def __str__(self):
        return f"File: {self.title}"
    
    
   

class MVHallFiles(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='mvhall_uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
    
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    USN = models.CharField(max_length=10)
    USERNAME_FIELD = "email"
    is_registered=models.BooleanField(default=False)
    year=models.CharField(max_length=4,default='2025')
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
