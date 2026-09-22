from rest_framework import serializers
from .models import Service
from .models import Staff
from .models import TimeSlot
from .models import Booking
from rest_framework.exceptions import ValidationError

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
        
        
class BookingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Booking
        fields=['id','first_name','last_name','phone_number','service','time_slot']
        extra_kwargs={
            'time_slot':{
                'validators':[]
            }
        }
    def validate(self,data):
       time_slot = data['time_slot']
       if time_slot.is_open ==False:
           raise ValidationError("Sorry, this slot is already booked!")
       return data
        