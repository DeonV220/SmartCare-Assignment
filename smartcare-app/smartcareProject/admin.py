from django.contrib import admin
<<<<<<< HEAD
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Person, UserProfile, Doctor

from .forms import CustomUserCreationForm, LoginForm

# Register your models here.



class CustomUserAdmin(UserAdmin):
    form = CustomUserCreationForm
    add_form = LoginForm
    list_display = ['username', 'email', 'role']

    


# class PersonProfile(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name', 'email', 'birth_date']
@admin.register(Person)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name', 'email', 'birth_date'] 
    search_fields = ('name', 'email')   

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)




#admin.site.register(invoices)
# Weekly invoices
=======
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'username', 'email', 'birth_date')
    search_fields = ('firstname', 'lastname', 'username', 'email')

admin.site.register(Patient, PatientAdmin)




>>>>>>> 9438346da8a2c09c13b54b91260cb704c29434c3
