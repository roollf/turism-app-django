from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class schedulingTravel(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    from_place = models.CharField(max_length=100)
    to_place = models.CharField(max_length=100)
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField()
    note = models.CharField(max_length=250,null=True, blank=True)
    
    class Meta:
        db_table = 'schedulingtravel'
        
    def __str__(self):
        return self.title