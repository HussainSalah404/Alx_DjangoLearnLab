from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm

# Create your views here.

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created! You can now log in.")
            return redirect("login")  # Django’s built-in login
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})

@login_required
def profile(request):
    return render(request, "profile.html")