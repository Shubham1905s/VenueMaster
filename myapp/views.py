# from django.shortcuts import render,HttpResponse,redirect
# from .models import Booking
# # Create your views here.
# def home(request):
#     return render(request,'home.html')

# # def audi(request):
# #     return render(request,'audi.html')

# def success(request):
#     return render(request,'success.html')

# def audi(request):
#     if request.method == 'POST':
#         club_name = request.POST.get('clubs')
#         date = request.POST.get('date')
#         start_time = request.POST.get('from')
#         end_time = request.POST.get('to')

#         # Create and save the booking object
#         Booking = Booking.objects.create(
#             club_name=club_name,
#             date=date,
#             start_time=start_time,
#             end_time=end_time
#         )

#         # Optionally, you can redirect to a success page or do something else
#         return redirect('success.html')  # Replace 'success_page' with your URL name

#     return render(request, 'audi.html') 





from django.shortcuts import render, redirect
from .models import Booking

def home(request):
    return render(request, 'home.html')

def success(request):
    return render(request, 'success.html')

def audi(request):
    if request.method == 'POST':
        club_name = request.POST.get('clubs')
        date = request.POST.get('date')
        start_time = request.POST.get('from')
        end_time = request.POST.get('to')

        # Create and save the booking object
        Booking.objects.create(
            club_name=club_name,
            date=date,
            start_time=start_time,
            end_time=end_time
        )

        # Redirect to the success page
        return redirect('myapp:success')

    return render(request, 'audi.html')
