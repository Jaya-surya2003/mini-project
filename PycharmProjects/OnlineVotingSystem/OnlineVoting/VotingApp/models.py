from django.db import models

# Create your models here
class UserProfile(models.Model):
    username=models.CharField(max_length=100)
    emailid=models.EmailField()
    password=models.CharField(max_length=100)
    dob=models.DateField()
    gender=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
