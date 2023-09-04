from django.db import models

# Create your models here.
class Bookings(models.Model):
    name=models.CharField(max_length=255)
    no_of_nuests=models.IntegerField()
    BookingDate=models.DateTimeField()
    
    
class Menu(models.Model):
    title=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    inventory=models.IntegerField()
    