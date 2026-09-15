from rest_framework import serializers
from .models import Service
from .models import Staff
from .models import TimeSlot

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id','name','price','description']
        
        
        
class StaffSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True,read_only=True)
    class Meta:
        model = Staff
        fields = ['first_name','last_name','phone_number','role','services']
        
        
class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = ['id','staff','start_time','is_open']