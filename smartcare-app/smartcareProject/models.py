<<<<<<< HEAD
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth import get_user_model
=======
>>>>>>> 9438346da8a2c09c13b54b91260cb704c29434c3
from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.

    
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
         ('staff', 'Staff',),
         ('patient', 'Patient'),
         ('owner', 'Owner'), # this is the admin role
     ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='owner')

    
  

    def __str__(self):
        return self.username
    

# set permissions in data migration

# ownerprofile inherits super

# choices 
OCCUPATION =[
    ('nuse', 'Nurse'),
    ('doctor','Doctor'),
]

class UserProfile(AbstractUser):
    user = models.OneToOneField(get_user_model(), null=True, on_delete=models.CASCADE,swappable=True, related_name='user_profiles')
    groups = models.ManyToManyField(Group, blank=True, related_name='user_profiles')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='user_profiles')
    
    password = models.CharField(max_length=128, default='default_password',  null=True)

    def __str__(self):
<<<<<<< HEAD
        return str(self.user)


    


class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, null=True, on_delete=models.CASCADE, related_name='doctor_profile')
    name = models.CharField(max_length=30)

    
    
    def __str__(self):
        return f"{self.name} - {self.user.username}"


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    birth_date = models.DateField()
    # doctor = models.ForeignKey(Doctor, related_name='patients', null=True, on_delete=models.SET_NULL)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

# make person appear in the admin (user part)
=======
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
>>>>>>> 9438346da8a2c09c13b54b91260cb704c29434c3
