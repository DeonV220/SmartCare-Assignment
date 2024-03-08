from django import forms
from django.contrib.auth.forms import UserCreationForm
from smartcareProject.models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser


# creates the profile new user
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
<<<<<<< HEAD
        #CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']

# profile of login depening on the profile
class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser  
        fields = ['username', 'password'] 
        role = forms.ChoiceField(choices=[('staff', 'Staff'), ('patient', 'Patient'), ('owner', 'Owner')])


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email','password1', 'password2']

=======
        fields = ['username', 'email','password1', 'password2']
        
>>>>>>> 9438346da8a2c09c13b54b91260cb704c29434c3
class StaffLoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class PatientLoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
<<<<<<< HEAD

class AdminLoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
=======
    
class AdminLoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

>>>>>>> 9438346da8a2c09c13b54b91260cb704c29434c3
