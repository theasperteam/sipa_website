from django.shortcuts import render
from .models import *
# Create your views here.
def Index(request):
    error = False
    if request.method == 'POST':
        dd = request.POST
        name = dd['name']
        email = dd['email']
        phone = dd['phone']
        cat = dd['cat']
        Book_Appointment_Events.objects.create(Name=name, Email=email, Phone=phone, Category=cat)
        error = True

    d = {'error':error}
    return render(request, 'events-index.html', d)

def About(request):
    return render(request, 'events-about.html')

def Contact(request):
    error = False
    if request.method == 'POST':
        dd = request.POST
        name = dd['name']
        email = dd['email']
        phone = dd['phone']
        cat = dd['cat']
        message = dd['message']
        Contact_Form_Events.objects.create(Name=name, Email=email, Phone=phone, Category=cat, Message=message)
        error = True

    d = {'error': error}
    return render(request, 'events-contact.html', d)


def Corporate(request):
    return render(request, 'events-corporate.html')


def Gallery(request):
    return render(request, 'events-gallery.html')

def Government(request):
    return render(request, 'events-government.html')

def Wedding(request):
    return render(request, 'events-wedding.html')

def Sports(request):
    return render(request, 'events-sports.html')

def Cultural(request):
    return render(request, 'events-cultural.html')

def Team(request):
    return render(request, 'events-team.html')