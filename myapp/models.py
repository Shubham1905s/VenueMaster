from django.db import models

class Booking(models.Model):
    club_name = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.club_name} - {self.date} ({self.start_time} to {self.end_time})"
