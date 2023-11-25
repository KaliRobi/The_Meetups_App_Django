from django.contrib import admin
from .models import Meetups, Location, Participant


#add columns like this in admin
class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'meetup_id','location')
    list_filter =('title', 'event_date')
    prepopulated_fields = {'meetup_id':('title',)}

admin.site.register(Meetups, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)