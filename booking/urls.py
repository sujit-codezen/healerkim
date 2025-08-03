# booking/urls.py
from django.urls import path
from .views import available_time_slots, book_appointment

urlpatterns = [
    path('', available_time_slots, name='available_time_slots'),
    path('book_appointment/', book_appointment, name='book_appointment'),
]
