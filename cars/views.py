from django.shortcuts import render , redirect
from users.forms import ContactForm
from .models import Car
from django.contrib import messages

def home(request):
    cars = Car.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('/#contact-us')
        else:
            form = ContactForm()
    return render(request, 'cars/home.html', {'cars': cars})

def about(request):
    return render(request, 'cars/about.html')

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})