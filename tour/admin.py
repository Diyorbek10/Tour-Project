from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    list_per_page = 10
    search_fields = ['name']
admin.site.register(Category,CategoryAdmin)


class TourAdmin(admin.ModelAdmin):
    list_display = ['name','start_date','end_date','agency','price','seats']
    list_per_page = 10
    list_editable = ['price','seats']
    search_fields = ['name','short_description','description']
admin.site.register(Tour, TourAdmin)


class TourServiceAdmin(admin.ModelAdmin):
    list_display = ['name','tour']
    list_per_page = 10
    search_fields = ['name','description']
admin.site.register(TourService,TourServiceAdmin)


class MediaTourAdmin(admin.ModelAdmin):
    list_display = ['image','video','tour']
    list_per_page = 10
admin.site.register(MediaTour,MediaTourAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['tour','user']
    search_fields = ['tour','user','text']
    list_per_page = 10
admin.site.register(Feedback,FeedbackAdmin)