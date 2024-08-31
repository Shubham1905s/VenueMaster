
from django.shortcuts import render, redirect
from .models import Booking
from django.http import HttpResponse
from .models import *
from .forms import ModelForm
from .forms import CreateUserForm
# from .filters import OrderFilter
# from .filters import OrderFilter 
# from .models import User
from django.contrib import messages
# from booking.models import Booking
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login as auth_login ,logout



def home(request):
    servicedata= Booking.objects.all().order_by('date')
    context={
        'bookings' : servicedata
    }
    return render(request, 'home.html',context)


# this is done for the login and registration of the page a king of demonstration
# def registerPage(request):
#     form = CreateUserForm()
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('username')
#             messages.success(request, 'Account Created Successfully for '+ user)
#             return redirect('myapp:loginPage')
#         else:
#             messages.error(request, 'Registration Failed. ')
#             error_message = 'registration failed. Please correct the errors below.'
#             return render(request,'registerPage.html')           
#     # context = {'form' : form}
#     return render(request,'registerPage.html',{'form':form})


#chatgpt

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
# this page is for the login

    #after successfull login i should be redirected to the audi page which is audi.html
# def loginPage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         # username = request.POST['username']
#         password = request.POST.get('password')
#         # password = request.POST['password']
#         print(username, password)
#         user = authenticate(request,username = username, password = password)
        
#         if user is not None:
#             login(request, user)
#             print("success")
#             # return JasonResponse({'data':'success'})
#             return redirect('myapp:audi')
#     context = {}
#     return render(request,'loginPage.html',context)


#chatgpt
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  # Using the correct login function
            print("success")
            return redirect('myapp:audi')
    return render(request, 'loginPage.html')
# username = "sanju"
# password = "sanju12345678"

# # Attempt to authenticate the user with these credentials
# user = authenticate(username=username, password=password)

# Check if authentication was successful
# print(user)
def success(request):
    return render(request, 'success.html')

# def login(request):
#     return render(request, 'login.html')

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
