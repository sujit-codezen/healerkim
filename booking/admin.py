# admin.py
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django import forms
from .models import Booking

class DateRangeForm(forms.Form):
    start_date = forms.DateField(widget=admin.widgets.AdminDateWidget())
    end_date = forms.DateField(widget=admin.widgets.AdminDateWidget())

class DateRangeFilter(admin.filters.SimpleListFilter):
    title = _('Date Range')
    parameter_name = 'date_range'

    def lookups(self, request, model_admin):
        return (
            ('today', _('Today')),
            ('tomorrow', _('Tomorrow')),
            ('this_week', _('This Week')),
            ('this_month', _('This Month')),
            ('this_year', _('This Year')),
        )

    def queryset(self, request, queryset):
        today = timezone.now().date()
        if self.value() == 'today':
            return queryset.filter(date_and_time__date=today)
        elif self.value() == 'tomorrow':
            tomorrow = today + timezone.timedelta(days=1)
            return queryset.filter(date_and_time__date=tomorrow)
        elif self.value() == 'this_week':
            week_end = today + timezone.timedelta(days=(6 - today.weekday()))
            return queryset.filter(date_and_time__date__range=[today, week_end])
        elif self.value() == 'this_month':
            month_end = today.replace(day=1) + timezone.timedelta(days=32 - today.day)
            return queryset.filter(date_and_time__date__range=[today, month_end])
        elif self.value() == 'this_year':
            year_end = today.replace(month=1, day=1) + timezone.timedelta(days=365)
            return queryset.filter(date_and_time__date__range=[today, year_end])
        return queryset.filter(date_and_time__date=today)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'contact_no', 'email', 'date_and_time', 'booking_status', 'created_on')
    list_filter = ('date_and_time', DateRangeFilter, 'booking_status')
    search_fields = ('customer_name', 'contact_no', 'email')
    ordering = ['-created_on']

admin.site.register(Booking, BookingAdmin)
