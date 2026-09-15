from django.urls import path,include
from .views import ServiceListView,StaffListView,TimeSlotListView

urlpatterns=[
    path('services/',ServiceListView.as_view(),name='service-list'),
    path('staff/',StaffListView.as_view(),name='staff-list'),
    path('timeslots/',TimeSlotListView.as_view(),name='time-slot')
]