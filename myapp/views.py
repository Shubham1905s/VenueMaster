
from django.shortcuts import render, redirect
from .models import Booking
from django.http import HttpResponse
from .models import *
from .forms import ModelForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login as auth_login ,logout

def home(request):
    servicedata= Booking.objects.all().order_by('date')
    context={
        'bookings' : servicedata
    }
    return render(request, 'home.html',context)


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account Created Successfully for {user}')
            return redirect('myapp:loginPage')
        else:
            messages.error(request, 'Registration Failed. Please correct the errors below.')
            return render(request, 'registerPage.html', {'form': form})
    
    return render(request, 'registerPage.html', {'form': form})

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  
            print("success")
            return redirect('myapp:audi')
    return render(request, 'loginPage.html')

def logoutUser(request):
    logout(request)
    return redirect('myapp:home')
def success(request):
    return render(request, 'success.html')

def errorbook(request):
    return render(request, 'errbook.html')


def audi(request):
    servicedata = Booking.objects.all().order_by('date')
    data={
        'servicedata': servicedata
    }
    if request.method == 'POST':
        club_name = request.POST.get('clubs')
        date = request.POST.get('date')
        start_time = request.POST.get('from')
        end_time = request.POST.get('to')
        
        conf_bookings = Booking.objects.filter(
            date = date,
            start_time__lt = end_time,
            end_time__gt = start_time
        )
        if conf_bookings.exists():
            messages.error(request,f'Time slot from {start_time} to {end_time} is already booked by {club_name}. Please check for some other time slot :)')
            return render(request,'errbook.html',data)
        Booking.objects.create(
            club_name=club_name,
            date=date,
            start_time=start_time,
            end_time=end_time
        )
       
        return redirect('myapp:audi')
    context ={
        'bookings':servicedata,
    }
    return render(request, 'audi.html', context)
