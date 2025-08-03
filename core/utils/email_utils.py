from django.core.mail import send_mail

def send_email(email, selected_datetime):
    subject = 'Booking Confirmation'
    message = f'Thank you for booking. Your appointment is scheduled for {selected_datetime}.'
    from_email = 'nepal@gmail.com'
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list, fail_silently=False,)
