from django.db import models
from django.conf import settings
from cars.models import Car

class Rental(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def _str_(self):
        return f"{self.user} renting {self.car} from {self.start_date} to {self.end_date}"