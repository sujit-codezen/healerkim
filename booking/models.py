from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from datetime import time, datetime, timedelta
import pytz
from django.utils import timezone

def validate_date_and_time(reservation_date_and_time):
    pass


BOOKING_STATUS_CHOICES = [
    ('Booked', 'Booked'),
    ('Pending', 'Pending'),
    ('Cancalled', 'Cancalled'),
    ('Completed', 'Completed'),
]

class Booking(models.Model):
    customer_name = models.CharField(max_length=20, null=True)
    contact_no = models.CharField(max_length=20, null=True)
    email = models.EmailField()
    date_and_time = models.DateTimeField(null=True, validators=[validate_date_and_time])
    booking_status = models.CharField(
        max_length=50,
        choices=BOOKING_STATUS_CHOICES,
        default = "Pending"
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('date_and_time',)
        ordering = ["-created_on"]

    def __str__(self):
        return f' User {self.customer_name} has made a booking \
                   form {self.contact_no}\
                   and {self.email} customers\
                   for {self.date_and_time}.'

    @classmethod
    def get_available_time_slots(cls, selected_date):
        start_time_weekdays = time(19, 15)
        end_time_weekdays = time(21, 0)

        start_time_weekends = time(12, 0)
        end_time_weekends = time(19, 0)

        time_interval = timedelta(minutes=15)

        selected_datetime = timezone.make_aware(datetime.combine(selected_date, start_time_weekdays))

        available_time_slots = []

        while selected_datetime.time() <= end_time_weekdays:
            if (
                not cls.objects.filter(date_and_time=selected_datetime).exists()
                and selected_datetime > timezone.now()
            ):
                available_time_slots.append(selected_datetime)
            selected_datetime += time_interval

        if selected_date.weekday() in [5, 6]:
            selected_datetime = timezone.make_aware(datetime.combine(selected_date, start_time_weekends))

            while selected_datetime.time() <= end_time_weekends:
                # Check if the time slot is not occupied and is in the future
                if (
                    not cls.objects.filter(date_and_time=selected_datetime).exists()
                    and selected_datetime > timezone.now()
                ):
                    # Append the available time slot to the list
                    available_time_slots.append(selected_datetime)
                # Move to the next time slot based on the defined interval
                selected_datetime += time_interval

        # Return the list of available time slots
        return available_time_slots
