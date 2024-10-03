
from django.shortcuts import render, redirect
from .models import Booking
from django.http import HttpResponse
from .models import *
from .forms import ModelForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login as auth_login ,logout
from django.contrib.auth.decorators import login_required
from .models import AuditoriumInfo,MVHallInfo
from django.http import HttpResponseRedirect
from .forms import MVHallUploadFileForm

from .forms import UploadFileForm
def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myapp:success')  # Redirect to the success page
        else:
            return render(request, "upload.html", {"form": form, "error": "Failed to upload file. Please try again."})
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})


def upload_mvhall_file(request):
    if request.method == 'POST':
        form = MVHallUploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Replace with your actual success page
    else:
        form = MVHallUploadFileForm()
    return render(request, 'upload_mvhall_file.html', {'form': form})

def home(request):
    auditorium_bookings =  Booking.objects.all().order_by('date')
    mvhall_bookings =  MVHallBooking.objects.all().order_by('date')
   
    context={
        'auditorium_bookings': auditorium_bookings,
        'mvhall_bookings': mvhall_bookings,
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
            return render(request, 'registererror.html', {'form': form})
    
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


def audi(request):
    servicedata = Booking.objects.all().order_by('date')
    info = AuditoriumInfo.objects.first()  
    
    if request.method == 'POST':
        club_name = request.POST.get('clubs')
        date = request.POST.get('date')
        start_time = request.POST.get('from')
        end_time = request.POST.get('to')
        
        conf_bookings = Booking.objects.filter(
            date=date,
            start_time__lt=end_time,
            end_time__gt=start_time
        )
        
        if conf_bookings.exists():
            messages.error(request, f'Time slot from {start_time} to {end_time} is already booked by {club_name}. Please check for some other time slot :)')
            return render(request, 'errbook.html', {'servicedata': servicedata, 'auditorium_info': info})

        Booking.objects.create(
            club_name=club_name,
            date=date,
            start_time=start_time,
            end_time=end_time
        )
        return redirect('myapp:audi')

    context = {
        'bookings': servicedata,
        'auditorium_info': info,  
    }
    return render(request, 'audi.html', context)


def audi_view(request):
    info = AuditoriumInfo.objects.first()  
    context = {
        'auditorium_info': info
    }
    return render(request, 'audi.html', context)


def MVhall(request):
    mvhall_bookings = MVHallBooking.objects.all().order_by('date')
    mvhall_info = MVHallInfo.objects.first()
    context = {
        'bookings': mvhall_bookings,
        'mvhall_info': mvhall_info,
    }
    if request.method == 'POST':
        club_name = request.POST.get('clubs')
        date = request.POST.get('date')
        start_time = request.POST.get('from')
        end_time = request.POST.get('to')
        
        conf_bookings = MVHallBooking.objects.filter(
            date=date,
            start_time__lt=end_time,
            end_time__gt=start_time
        )
        if conf_bookings.exists():
            messages.error(request, f'Time slot from {start_time} to {end_time} is already booked by {club_name}. Please check for some other time slot :)')
            return render(request, 'errbook.html', context)
        MVHallBooking.objects.create(
            club_name=club_name,
            date=date,
            start_time=start_time,
            end_time=end_time
        )
        return redirect('myapp:MVhall')
    
    return render(request, 'MVhall.html', context)

def errorbook(request):
    return render(request, 'errbook.html')

def registererror(request):
    return render(request, 'registererror.html')

def regMVhall(request):
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
            return render(request, 'registererror.html', {'form': form})
    context = {'form': form}
    return render(request, 'registerPage.html', {'form': form},context)

def loginPageMVhall(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  
            print("success")
            return redirect('myapp:MVhall')
        else :
            messages.error(request, 'Invalid credentials')
            # return redirect('myapp:loginPageMVhall')
    return render(request, 'loginPage.html')



# def regMVhall(request):
#     form = CreateUserForm()
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('username')
#             messages.success(request, f'Account Created Successfully for {user}')
#             return redirect('myapp:loginPageMVhall')
#         else:
#             messages.error(request, 'Registration Failed. Please correct the errors below.')
#             return render(request, 'registererror.html', {'form': form})
#     context = {'form': form}
#     return render(request, 'regMVhall.html', {'form': form},context)

# def loginPageMVhall(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         print(username, password)
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             auth_login(request, user)  
#             print("success")
#             return redirect('myapp:MVhall')
#         else :
#             messages.error(request, 'Invalid credentials')
#             # return redirect('myapp:loginPageMVhall')
#     return render(request, 'loginPageMVhall.html')


