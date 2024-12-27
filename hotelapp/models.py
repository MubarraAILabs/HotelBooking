from django.db import models

# Create your models here.
class Hotel(models.Model):
    hotelId = models.AutoField(primary_key=True)
    hotelName = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    hotelType = models.CharField(max_length=100)
    rating = models.IntegerField()
    contact = models.CharField(max_length=100)
    hotel_image = models.ImageField(null=True, blank=True, upload_to="images/")
    

class Category(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_No = models.IntegerField()
    roomType = models.CharField(max_length=100)
    price_per_room = models.FloatField(default=0.0)
    available_rooms = models.IntegerField()