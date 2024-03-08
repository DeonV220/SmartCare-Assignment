from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'username', 'email', 'birth_date')
    search_fields = ('firstname', 'lastname', 'username', 'email')

admin.site.register(Patient, PatientAdmin)




