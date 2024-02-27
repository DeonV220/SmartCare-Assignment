from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

# Role selection view (for new users)
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

def login(request):
    # Your login view logic here
    return render(request, 'login.html')