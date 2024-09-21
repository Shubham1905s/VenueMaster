from django.db import models

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
