from django.contrib import admin
from siteapp.models import schedulingTravel
from siteapp.models import travelInsurance
from siteapp.models import commentsAngency


class schedulingTravelAdmin(admin.ModelAdmin):
    list_display = ('title', 'from_place', 'to_place')


class travelInsuranceAdmin(admin.ModelAdmin):
    list_display = ('user', 'passport', 'birthday')
    
    
class commentsAngencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')
    

admin.site.register(schedulingTravel, schedulingTravelAdmin)
admin.site.register(travelInsurance, travelInsuranceAdmin)
admin.site.register(commentsAngency, commentsAngencyAdmin)
