from django.shortcuts import render
from customerapp.models import Customer
from .models import Admin
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password

# Create your views here.
def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        type = request.POST.get('type')

        if type == 'user':
            cust=Customer.objects.get(email=email)

            if cust:

                flag=check_password(password,cust.password)
                if flag:
                    request.session['username'] = email
                    return render(request, 'index.html')
                   # return HttpResponse("<h1>Success</h1>")
            else:
                return HttpResponse("<h1>Email not found</h1>")

        if type == 'admin':
            admin=Admin.objects.get(email=email)
            if admin:
                if password == admin.password:
                    request.session['email'] = email
                    return render(request, 'index.html')
                    #return HttpResponse("<h1>Success</h1>")
                else:
                    return HttpResponse("<h1>Password not match</h1>")
    return render(request, 'login.html')

def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return render(request, 'index.html')