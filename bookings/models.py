from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=90)
    price= models.DecimalField(max_digits=6,decimal_places=2)
    duration_minutes = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} - {self.price} - {self.duration_minutes}"


class Staff(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=15)
    services = models.ManyToManyField(Service)   
    
    role = models.CharField(
    max_length=20,
    choices=[
        ("admin", "Admin"),
        ("receptionist", "Receptionist"),
    ],
    default="receptionist"
)
    def __str__(self):
            return f"{self.first_name} {self.last_name}"

class TimeSlot(models.Model):
    staff= models.ForeignKey(Staff,on_delete=models.CASCADE) 
    start_time = models.DateTimeField()
    is_open = models.BooleanField(default=True)
    def __str__(self):
            return f"{self.staff.first_name} - {self.start_time}"
    
class Booking(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=15)
    service= models.ForeignKey(Service,on_delete=models.PROTECT)
    time_slot= models.OneToOneField(TimeSlot,on_delete=models.CASCADE)
    
    def __str__(self):
            return f"{self.first_name} {self.last_name} booked {self.service}"
    