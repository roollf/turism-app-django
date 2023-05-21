from django.contrib import admin
from siteapp.models import schedulingTravel

# Register your models here.


class schedulingTravelAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'from_place', 'to_place')

admin.site.register(schedulingTravel, schedulingTravelAdmin)
