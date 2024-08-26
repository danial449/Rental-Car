from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'make' , 'model', 'year', 'price_per_day','available')

admin.site.register(Car, CarAdmin)
