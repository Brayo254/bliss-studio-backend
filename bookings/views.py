from django.shortcuts import render
from rest_framework import generics
from .models import Service
from .models import TimeSlot
from .models import Staff
from .serializers import ServiceSerializer
from .serializers import StaffSerializer
from .serializers import TimeSlotSerializer

# Create your views here.
class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
    
class StaffListView(generics.ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    
    
class TimeSlotListView(generics.ListAPIView):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer
