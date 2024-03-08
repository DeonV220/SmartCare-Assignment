from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('staff', 'Staff'),
        ('patient', 'Patient'),
        ('admin', 'Admin'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='')

    def __str__(self):
        return self.username

class Patient(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
