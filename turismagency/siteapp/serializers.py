from rest_framework import serializers
from .models import *

class schedulingTravelView(serializers.ModelSerializer):
    class Meta:
        model = schedulingTravel
        fields = '__all__'