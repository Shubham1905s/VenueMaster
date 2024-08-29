
from django.shortcuts import render, redirect
from .models import Booking
from django.http import HttpResponse
from .models import *
from .forms import ModelForm
from .forms import CreateUserForm
# from .filters import OrderFilter 
# from .models import User
from django.contrib import messages
# from booking.models import Booking
from django.contrib.auth.forms import UserCreationForm

def home(request):
    servicedata= Booking.objects.all().order_by('date')
    context={
        'bookings' : servicedata
    }
    return render(request, 'home.html',context)


# this is done for the login and registration of the page a king of demonstration
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('myapp:registerPage')
        else:
            # messages.error(request, 'Registration Failed. ')
            error_message = 'registration failed. Please correct the errors below.'
            return render(request,'registerPage.html',{'form':form,'error_message':error_message})           
    # context = {'form' : form}
    return render(request,'registerPage.html',{'form':form})

# this page is for the login

def loginPage(request):
    context = {}
    return render(request,'register.html',context)

def success(request):
    return render(request, 'success.html')

def login(request):
    return render(request, 'login.html')

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
        # Redirect to the success page
        return redirect('myapp:success')
    context ={
        'bookings':servicedata,
    }
    return render(request, 'audi.html', context)
