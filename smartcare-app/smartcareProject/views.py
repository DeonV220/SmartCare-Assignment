from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, StaffLoginForm, PatientLoginForm, AdminLoginForm
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

# Role selection view
def select_role(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Handle form submission logic
            user = form.save()
            # Redirect to the login page
            return redirect('login')  # Use the correct name for the login URL
    else:
        form = CustomUserCreationForm()

    return render(request, 'select_role.html', {'form': form})

def staff_login(request):
    if request.method == 'POST':
        form = StaffLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to staff dashboard or any other staff-specific page
                return redirect('staff_dashboard')
    else:
        form = StaffLoginForm()
    
    return render(request, 'staff_login.html', {'form': form})

def patient_login(request):
    if request.method == 'POST':
        form = PatientLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to patient dashboard or any other patient-specific page
                return redirect('patient_dashboard')
    else:
        form = PatientLoginForm()

    return render(request, 'patient_login.html', {'form': form})

def patient_signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirect to patient dashboard or any other patient-specific page
            return redirect('patient_dashboard')
    else:
        form = CustomUserCreationForm()

    return render(request, 'patient_signup.html', {'form': form})

def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to admin dashboard or any other admin-specific page
                return redirect('admin_dashboard')
    else:
        form = AdminLoginForm()

    return render(request, 'admin_login.html', {'form': form})


