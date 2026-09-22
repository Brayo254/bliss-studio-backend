from django.urls import path,include
from .views import ServiceListView,StaffListView,TimeSlotListView,BookingCreateView,BookingListView

urlpatterns=[
    path('services/',ServiceListView.as_view(),name='service-list'),
    path('staff/',StaffListView.as_view(),name='staff-list'),
    path('timeslots/',TimeSlotListView.as_view(),name='time-slot'),
    path('bookings/',BookingCreateView.as_view(),name='booking'),
    path('bookings/all/',BookingListView.as_view(),name='booking-list')
]