from django.shortcuts import render
from .models import Booking
from datetime import datetime
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import redirect
from core.utils.email_utils import send_email
from .tasks import send_booking_reminder
import pytz

def available_time_slots(request):
    print(timezone.now())
    if request.method == 'POST':
        selected_date_str = request.POST.get('selected_date')
        selected_date = datetime.strptime(selected_date_str, '%Y-%m-%d').date()
        
        available_time_slots = Booking.get_available_time_slots(selected_date)
        return render(request, 'booking/booking.html', {'available_time_slots': available_time_slots})
    else:
        return render(request, 'booking/booking.html')


def book_appointment(request):
    if request.method == 'POST':
        selected_datetime_str = request.POST.get('selected_datetime')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        contact_no = request.POST.get('contact_no')
        if (selected_datetime_str and full_name and email and contact_no) != '':
            selected_datetime = datetime.strptime(selected_datetime_str, '%Y-%m-%d %H:%M:%S')
            booking = Booking.objects.create(customer_name=full_name,contact_no=contact_no,email=email,date_and_time=selected_datetime)
            messages.success(request, "Booked Successfully")
            print(timezone.timedelta(seconds=20))
            local_time = booking.date_and_time
            local_timezone = pytz.timezone('Asia/Kathmandu')
            utc_time = local_timezone.localize(local_time).astimezone(pytz.utc)
            print(utc_time)
            send_booking_reminder.apply_async((booking.pk,), eta=utc_time)
            return redirect('/')
        else:
            messages.warning(request, "All fields Required")
            return redirect('/booking/available_time_slots/')
    return redirect('error_page') 
