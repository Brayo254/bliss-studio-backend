from django.contrib import admin
from .models import Service,Staff,TimeSlot,Booking


# Register your models here.
admin.site.register(Service)
admin.site.register(Staff)
admin.site.register(TimeSlot)
admin.site.register(Booking)