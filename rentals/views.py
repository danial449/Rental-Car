from django.shortcuts import render
from .models import Rental

def rental_list(request):
    rentals = Rental.objects.all()
    return render(request, 'rentals/rental_list.html', {'rentals': rentals})