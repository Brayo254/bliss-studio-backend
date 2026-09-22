from django.shortcuts import render
from rest_framework import generics,permissions
from .models import Service
from .models import TimeSlot
from .models import Staff
from .models import Booking
from .serializers import ServiceSerializer
from .serializers import StaffSerializer
from .serializers import TimeSlotSerializer
from .serializers import BookingSerializer


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


class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingListView(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]