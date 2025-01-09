from django.db import models
from customerapp.models import Customer

# Create your models here.
class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    address = models.TextField()
    type = models.CharField(max_length=100)
    rating = models.FloatField()
    contact = models.CharField(max_length=15)
    image = models.ImageField(upload_to='hotel_images/', null=True, blank=True)

class Category(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_No = models.IntegerField()
    roomType = models.CharField(max_length=100)
    price_per_rooms = models.FloatField(default=0.0)
    available_rooms = models.IntegerField()

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    no_of_room = models.FloatField(default=0.0)
    no_of_people = models.IntegerField() 
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    total_price = models.FloatField(default=0.0)

class BookingConfirm(models.Model):
    ordernumber = models.CharField(max_length=100)
    orderdate = models.DateTimeField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6, null=True, blank=True)