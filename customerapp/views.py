from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.hashers import make_password

# Create your views here.
def addCustomer(request):
    if request.method == 'POST':
        name_customer = request.POST['name_customer']
        email = request.POST['email']
        password = request.POST['password']
        passw = make_password(password)
        phone_number = request.POST['phone_number']
        AadharId = request.POST['AadharId']
        address_customer = request.POST['address_customer']
        customer = Customer(name_customer=name_customer, email=email, password=passw, phone_number=phone_number, AadharId=AadharId, address_customer=address_customer)
        customer.save()
        return HttpResponse("<h1>Success ....</h1>")
    return render(request, 'add_customer.html')

def updateCustomer(request):
    if request.method == 'POST':
        name_customer = request.POST['name_customer']
        email = request.POST['email']
        password = request.POST['password']
        phone_number = request.POST['phone_number']
        AadharId = request.POST['AadharId']
        address_customer = request.POST['address_customer']
        data=Customer(name_customer=name_customer, email=email, password=password, phone_number=phone_number,AadharId=AadharId, address_customer=address_customer,)
        data.save()
        return HttpResponse("<h1>Success....</h1>")
    return render(request, 'update_customer.html')

def viewCustomers(request):
    customers = Customer.objects.all()
    return render(request, 'customers_list.html', {'customers': customers})

def editCustomer(request, email):
    data_edit=Customer.objects.filter(email=email)
    return render(request, 'update_customer.html', {'customer_update': data_edit})

def deleteCustomer(request, email):
    Customer.objects.filter(email=email).delete()
    return HttpResponse("<h1>Success....</h1>")
