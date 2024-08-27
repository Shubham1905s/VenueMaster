from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('club_name', 'date', 'start_time', 'end_time')


# admin.site.register(authentication)
# admin.site.register(User)