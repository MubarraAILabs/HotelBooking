from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def saveHotels(request):
    if request.method=='POST':
        hname=request.POST['hotelName']
        hlocation=request.POST['location']
        htype=request.POST['hotelType']
        hrating=request.POST['rating']
        hcontact=request.POST['contact']
        himage=request.FILES['hotel_image']
        new_hotel=Hotel(hotelName=hname,location=hlocation,hotelType=htype,rating=hrating,contact=hcontact,hotel_image=himage)
    #name from models = name from function saveHotels
        Hotel.save(new_hotel)
        return HttpResponse("<h1>Success ....</h1>")
    else:
        return render(request, 'AddHotels.html')