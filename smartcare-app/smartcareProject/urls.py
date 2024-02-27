from django.contrib import admin
from django.urls import path, include
from .views import select_role, staff_login, patient_login, admin_login

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', select_role, name='select_role'),
    path('login/staff/', staff_login, name='staff_login'),
    path('login/patient/', patient_login, name='patient_login'),
    path('login/admin/', admin_login, name='admin_login'),
]