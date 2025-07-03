from django.contrib import admin
from .models import Booking,MVHallBooking
from .models import AuditoriumInfo,MVHallInfo,AuditoriumFiles
# from .models import UploadFileForm
from django.contrib.auth.models import User
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('club_name', 'date', 'start_time', 'end_time')
    
admin.site.register(MVHallBooking)
admin.site.register(AuditoriumInfo)
admin.site.register(MVHallInfo)

@admin.register(AuditoriumFiles)
class UploadFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'file')
    
from .models import MVHallFiles
# @admin.register(MVHallUploadFile)
class MVHallUploadFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')  # Display these fields in the admin list view
    search_fields = ('title',)  # Enable search by title

admin.site.register(MVHallFiles, MVHallUploadFileAdmin)