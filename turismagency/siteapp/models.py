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
    
    
class travelInsurance(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    passport = models.CharField(max_length=30)
    birthday = models.DateField()
    type_trip = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'travelInsurance'
        
    def __str__(self):
        return self.user
    
    
class commentsAngency(models.Model):
    
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    comment = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'commentsAngency'
        
    def __str__(self):
        return self.name