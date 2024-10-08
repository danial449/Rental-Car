from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
   email = models.EmailField(null=True , unique=True)
   mobile_no = models.CharField(max_length=11 ,null=True, blank=True)
   is_email_verified = models.BooleanField(default=False)
   email_verification_token = models.CharField(max_length=200 ,blank=True, null=True)

   def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , blank=True, null=True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    username = models.CharField(max_length = 30)
    email = models.EmailField(null=True , unique=True)
    mobile_no = models.CharField(max_length=11, null=True, blank=True)

    def __str__(self):
        return self.username
    
class ContactUs(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField(null=False , unique=False)
    message = models.TextField(max_length = 500)

    def __str__(self):
        return self.message