from django.contrib import admin
from .models import Booking,MVHallBooking
from .models import AuditoriumInfo,MVHallInfo

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('club_name', 'date', 'start_time', 'end_time')
    
admin.site.register(MVHallBooking)
admin.site.register(AuditoriumInfo)
admin.site.register(MVHallInfo)