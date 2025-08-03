from django.shortcuts import render, HttpResponse,redirect,get_object_or_404,reverse

from .models import Contact
from django.contrib import messages


def contact(request):
    context = {
        'user': 'John',  
        'page_title': 'Home Page',
    }
    return render(request, 'contact/contact.html', context)


def addContact(request):
    if request.method == "POST":

        full_name = request.POST.get("full_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")
        page = request.POST.get("page")

        if full_name=='' or phone=='' or email=='' or message=='':
            messages.warning(request, "All fields Required")
            if page == "contact":
                return redirect('/contact/')
            return redirect('/#contact')

        else:
            newContact = Contact(full_name=full_name, phone=phone, email=email, message=message)
            newContact.save()
            messages.success(request, "Message Sent Successfully.")
            if page == "contact":
                return redirect('/contact/')
            return redirect('/#contact')
    else:
        return redirect('/#notfound')