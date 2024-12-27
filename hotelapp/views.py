from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def saveHotels(request):
    if request.method=='POST':
        hname=request.POST['hotelName']
        hlocation=request.POST['location']
        haddress=request.POST['address']
        htype=request.POST['hotelType']
        hrating=request.POST['rating']
        hcontact=request.POST['contact']
        himage=request.FILES.get('hotel_image')
        new_hotel=Hotel(hotelName=hname,address=haddress,location=hlocation,hotelType=htype,rating=hrating,contact=hcontact,hotel_image=himage)
    #name from models = name from function saveHotels
        Hotel.save(new_hotel)
        return HttpResponse("<h1>Success ....</h1>")
    else:
        return render(request, 'AddHotels.html')

def showHotels(request):
    data = Hotel.objects.all()
    return render(request, 'hotelList.html', {'hotels': data})

def updateHotels(request):
    if request.method=='POST':
        hId=request.POST['hotelId']
        hname=request.POST['hotelName']
        hlocation=request.POST['location']
        haddress=request.POST['address']
        htype=request.POST['hotelType']
        hrating=request.POST['rating']
        hcontact=request.POST['contact']
        himage=request.FILES.get('hotel_image')
        data=Hotel.objects.filter(hotelId=hId)
        data.update(hotelName=hname,address=haddress,location=hlocation,hotelType=htype,rating=hrating,contact=hcontact,hotel_image=himage)
    #name from models = name from function saveHotels
        return HttpResponse("<h1>Success ....</h1>")
    else:
        return render(request, 'updateHotel.html')
    
def deleteHotels(request, id):
    data=Hotel.objects.filter(hotelId=id)
    data.delete()
    return HttpResponse("<h1>Success ....</h1>")
def editHotels(request, id):
        data=Hotel.objects.get(hotelId=id)
        return render(request, 'updateHotel.html', {'hotel': data})