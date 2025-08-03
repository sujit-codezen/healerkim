from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from .models import Booking

@shared_task
def send_booking_reminder(booking_id):
    try:
        booking = Booking.objects.get(pk=booking_id)
        send_mail(
            'Booking Reminder',
            f'Your booking is scheduled for {booking.date_and_time}.',
            '10sujitkhanal@gmail.com',
            [booking.email],
            fail_silently=True,
        )
    except Booking.DoesNotExist:
        pass