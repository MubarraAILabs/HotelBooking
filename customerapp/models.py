from django.db import models

# Create your models here.
class Customer(models.Model):
    name_customer = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique="True")
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    AadharId = models.CharField(max_length=12)
    address_customer = models.CharField(max_length=200)

