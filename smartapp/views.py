from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages, auth
from django.shortcuts import render, redirect
from .models import Account
from django.contrib.auth import authenticate

# Create your views here.
def demo(request):
    return render(request,"index.html")
def login(request):
    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['pwd']
        fname=request.POST['nme']
        hname = request.POST['hname']
        city=request.POST['city']
        district=request.POST['district']
        pin_number=request.POST['pin']
        phone_number = request.POST['phn']
         #print(email,password,fname,hname,city,district,pin_number,phone_number)
        if Account.objects.filter(email=email).exists():
            messages.error(request, 'email already exists')
            return redirect('register')
        # elif Account.objects.filter(fname=fname).exists():
        #     messages.error(request, 'username already exists')
        #     return redirect('register')
        else:
            user=Account.objects.create_user(email=email, password=password, fname=fname, hname=hname, district=district, city=city, pin_number=pin_number, phone_number=phone_number)
            user.save()

    return render(request, 'registration.html')
