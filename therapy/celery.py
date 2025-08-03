import os
from django.conf import settings
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'therapy.settings')

app = Celery('therapy')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-booking-reminder-task': {
        'task': 'booking.tasks.send_booking_reminder',
        'schedule': crontab(hour=0, minute=1),  # Set the schedule as needed
    },
}

@app.task(bind=True)
def debug_task(self):
    print('Hello World')

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')