from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime  # Import the datetime module
from .models import *
from datetime import date

# Create your views here.
def index(request):
    return render(request, 'index.html')


def addhotel(request):
    if request.method == 'POST':
        name = request.POST['name']
        location = request.POST['location']
        address = request.POST['address']
        type = request.POST['type']
        rating = request.POST['rating']
        contact = request.POST['contact']
        image = request.FILES['image']
        hotel = Hotel(name=name, location=location, address=address, type=type, rating=rating, contact=contact, image=image)
        hotel.save()
        return HttpResponse("<h1>Success ....</h1>")
    return render(request, 'addHotels.html')

def viewhotels(request):
    hotels = Hotel.objects.all()
    return render(request, 'listHotels.html', {'hotels': hotels})

def updateHotel(request):
    if request.method=='POST':
        id=request.POST['id']
        name=request.POST['name']
        location=request.POST['location']
        address=request.POST['address']
        type=request.POST['type']
        rating=request.POST['rating']
        contact=request.POST['contact']
        image=request.FILES.get('image')
        #=Hotel.objects.filter(id=id)
        data=Hotel(id=id,name=name,location=location,address=address,type=type,rating=rating,contact=contact,image=image)
        #data.update(name=name,location=location,address=address,type=type,rating=rating,contact=contact,image=image)
    #name from models = name from function saveHotels
        data.save()
        return HttpResponse("<h1>Success ....</h1>")
    
    return render(request, 'update_hotel.html')

def editHotel(request, id):
        data_edit=Hotel.objects.get(id=id)
        return render(request, 'update_hotel.html', {'hotel_update': data_edit})
def deleteHotel(request, id):
     data_delete=Hotel.objects.get(id=id)
     data_delete.delete()
     return HttpResponse("<h1>Success ....</h1>")

###view for category

def addcategory(request,id):
    if request.method!='POST':
        hotels = Hotel.objects.get(id=id) 
        return render(request,'add_category.html',{'hotel_1': hotels})
    else:
        hotels = Hotel.objects.get(id=id) 
        room_No=request.POST['room_No']
        roomType=request.POST['roomType']
        price_per_rooms=request.POST['price_per_rooms']
        available_rooms=request.POST['available_rooms']
        cat=Category(hotel=hotels,room_No=room_No,roomType=roomType,price_per_rooms=price_per_rooms,available_rooms=available_rooms)
        cat.save()
        
        return HttpResponse("<h1>Successfully Added!</h1>")

# Category List
def category_list(request, id):
    categories = Category.objects.filter(id=id)
    categories = Category.objects.all()
    hotels = Hotel.objects.all()
    return render(request, 'list_category.html', {'categories': categories, 'hotels': hotels})


#Update category
def update_category(request, id):
    # Fetch the category instance to update
    category = Category.objects.get(id=id)
    hotel = category.hotel  # Fetch the associated Hotel instance

    if request.method != 'POST':
        # Render the form pre-filled with the category's current data
        return render(request, 'update_category.html', {
            'category': category,
            'hotel': hotel
        })
    else:
        # Update the fields with data from the POST request
        category.room_No = request.POST['room_No']
        category.roomType = request.POST['roomType']
        category.price_per_rooms = request.POST['price_per_rooms']
        category.available_rooms = request.POST['available_rooms']

        # If the hotel ID can be updated:
        hotel_id = request.POST.get('hotel_id')  # Optional: Fetch new hotel ID from the form
        if hotel_id:
            category.hotel = Hotel.objects.get(id=hotel_id)  # Update the associated hotel

        # Save the updated instance to the database
        category.save()
        
        return HttpResponse("<h1>Successfully Updated!</h1>")


# Delete category

def delete_category(request, id):
    category_delete = Category.objects.get(id=id)
    category_delete .delete()
    return HttpResponse("<h1>Successfully Deleted!</h1>")

######## Functions For Booking


def create_booking(request, id):
    room_category = Category.objects.get(id=id)
    # Fetch the specific room category using the provided ID
    if request.method!='POST':
        categorys = Category.objects.get(id=id)
        return render(request,'create_booking.html',{"c_data": categorys})

    else:
        email=request.session["username"]
        customer=Customer.objects.get(email=email)
        categorys = Category.objects.get(id=id)
        no_of_room=request.POST['no_of_room']
        no_of_people=request.POST['no_of_people']
        check_in=request.POST['check_in']
        check_out=request.POST['check_out']
        total_price=request.POST['total_price']


        # Validate `no_of_room`
        if not no_of_room:
            return HttpResponse("Number of rooms is required.")
        try:
            no_of_room = int(no_of_room)
        except ValueError:
            return HttpResponse("Invalid input for number of rooms.")

        # Fetch related objects
        customer = Customer.objects.get(email=email)
        hotel = room_category.hotel  # Directly fetch the hotel linked to the category

        # Check room availability
        available_rooms = room_category.available_rooms
        if no_of_room > available_rooms:
            return HttpResponse("Not enough rooms available.")

        # Calculate total price
        price_per_room = float(room_category.price_per_rooms)
        try:
            check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
            check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
        except ValueError:
            return HttpResponse("Invalid date format. Use YYYY-MM-DD.")

        days_difference = (check_out_date - check_in_date).days
        if days_difference <= 0:
            return HttpResponse("Check-out date must be after check-in date.")
        
        total_price = price_per_room * no_of_room * days_difference

        # Create the booking object
        booking = Booking.objects.create(
            customer=customer,
            hotel=hotel,
            room_category=room_category,
            no_of_people=no_of_people,
            no_of_room=no_of_room,
            check_in=check_in,
            check_out=check_out,
            total_price=total_price
        )

        booking.save()
        # Update the available rooms count
        room_category.available_rooms -= no_of_room
        room_category.save()

        return HttpResponse("<h1>Booking Successful!</h1>")
    
    # If GET request, render the booking creation form
    
def showBookings(request):
    emailid=request.session["username"]
    customer=Customer.objects.get(email=emailid)
    bookings = Booking.objects.filter(customer=customer)  
    return render(request, 'booking_list.html', {'bookings': bookings})

def deleteBooking(request, email):
    bookings = Booking.objects.filter(email=email)
    bookings.delete()  
    return HttpResponse("<h1>Successfully deleted the booking!</h1>")

def booking_table(request):
    if request.method == 'POST':
        c_date=date.today()
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        City = request.POST['City']
        pincode = request.POST['pincode']
        booking_table = BookingConfirm.objects.create( orderdate=c_date,first_name=first_name,last_name=last_name,address=address,City=City,pincode=pincode)
        booking_table.save()
   
        c_date=date.today()

        c_date1=str(c_date).replace("_","")
        OrderNo=c_date1+str(booking_table.id)
        booking_table.ordernumber=OrderNo
        booking_table.save()
        return render(request, 'Payment.html',{"data":booking_table})
        #return render(request,'bookingConfirmList.html')
    
    return render(request, 'booking_table.html')
  


def confirm_bookings(request):
    c_bookings = BookingConfirm.objects.all() # Example: Pass all bookings to the template
    return render(request, 'bookingConfirmList.html', {'c_bookings': c_bookings})