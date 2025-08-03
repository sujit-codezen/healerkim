from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        'page_name': 'home',
    }
    return render(request, 'home/home.html', context)