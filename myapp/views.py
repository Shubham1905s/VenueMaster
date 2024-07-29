
from django.shortcuts import render, redirect
from .models import Booking
from django.contrib import messages
# from booking.models import Booking
def home(request):
    return render(request, 'home.html')

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

        # Redirect to the success page
        return redirect('myapp:success')
    
    context ={
        'bookings':servicedata,
    }
    
    

    return render(request, 'audi.html', context)
