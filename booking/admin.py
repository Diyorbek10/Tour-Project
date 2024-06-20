from django.contrib import admin
from .models import Booking



class BookingAdmin(admin.ModelAdmin):
    list_display = ['user','seats_count','tour','status','phone_number','comment']
    list_per_page = 10 
    search_fields = ['comment']
admin.site.register(Booking,BookingAdmin)