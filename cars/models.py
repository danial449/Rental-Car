from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    cars_image = models.ImageField(upload_to='cars_images/' , null=True , blank=True)

    def _str_(self):
        return f"{self.make} {self.model} ({self.year})"