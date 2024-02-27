from django.contrib import admin
from django.urls import path, include
from .views import select_role, login

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', select_role, name='select_role'),
    path('login/', login, name='login'),

]