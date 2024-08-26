from django.urls import path
from .views import *

app_name = 'cars'

urlpatterns = [
    path("", home, name="home_view"),
    path("about/", about, name="about_view"),
    path("car-list/", car_list, name="car_list"),
]
