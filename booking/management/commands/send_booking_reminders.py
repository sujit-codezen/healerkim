from django.core.management.base import BaseCommand
from django.utils import timezone
from your_app.models import Booking
from your_app.tasks import send_booking_reminder

class Command(BaseCommand):
    help = 'Send email reminders for upcoming bookings'

    def handle(self, *args, **options):
        # Get bookings scheduled for the next 2 hours
        upcoming_bookings = Booking.objects.filter(
            date_and_time__gte=timezone.now(),
            date_and_time__lte=timezone.now() + timezone.timedelta(hours=2),
            reminder_sent=False
        )

        for booking in upcoming_bookings:
            send_booking_reminder.apply_async((booking.pk,), eta=booking.date_and_time - timezone.timedelta(hours=2))

            # Mark the reminder as sent to avoid sending it multiple times
            booking.reminder_sent = True
            booking.save()