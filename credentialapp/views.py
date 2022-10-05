from django.contrib import messages
from django.shortcuts import render, redirect
from .models import reg_user,log_user
from hashlib import sha256
# Create your views here.
def demo(request):
    request.session.flush()
    return render(request,"index.html")
#Login page
def login(request):
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        email=request.POST.get('email');
        password1 = request.POST.get('pwd');
        password2 = request.POST.get('cpwd');
        username = request.POST.get('nme');
        hname = request.POST.get('hname');
        city = request.POST.get('city');
        district = request.POST.get('district');
        pincode = request.POST.get('pin');
        phone = request.POST.get('phn');
        pswd=sha256(password2.encode()).hexdigest()
        if reg_user.objects.filter(email=email).exists():
            messages.success(request, 'Email already exists....!!!!')
            return redirect('register')
        else:
            user=reg_user(email=email,password=pswd,name=username,house_name=hname,city=city,district=district,pincode=pincode,phone_no=phone)
            log=log_user(email=email,password=pswd)
            user.save()
            log.save()
            messages.success(request, 'Your account has been successfully created..!!')
            return redirect('login')
    return render(request, 'registration.html')

# Login Function

def login(request):
    request.session.flush()
    if 'email' in request.session:
        return redirect(home)
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['pass']
        password2 = sha256(password.encode()).hexdigest()
        user=log_user.objects.filter(email=email,password=password2)
        if user:
            user_details=log_user.objects.get(email=email,password=password2)
            email=user_details.email
            request.session['email']=email
            messages.success(request, 'Login successfully..!!')
            return redirect('home')
           
        else:
            print("Invalid")
            messages.success(request, 'Email or Password Incorrect..!!')
    return render(request,'login.html')

#Customer Home Page
def home(request):
    if 'email' in request.session:
        email = request.session['email']
        return render(request,'home.html',{'email':email})
    return redirect(login)

# Customer Logout
def logout(request):
    if 'email' in request.session:
        request.session.flush()
    # auth.logout(request)
    return redirect(login)