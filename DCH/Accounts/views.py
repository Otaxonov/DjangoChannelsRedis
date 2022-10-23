from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm
from django.contrib import messages

# Create your views here.

def RegistrationView(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been successfully created. You are now able to Login")
            return redirect('accounts_login')
        messages.error(request, "Unsuccessful registration. Invalid information.")

    form = UserRegistrationForm()

    context  = {
        'title': 'User Create View',
        'form': form
    }

    return render(request, 'Accounts/registration.html', context)

def LoginView(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('chat_home')

        messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()

    context = {
        'title': 'Login',
        'form': form
    }

    return render(request, 'Accounts/login.html', context)

def LogoutView(request):

    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "You have successfully logged out.")

    return redirect('chat_home')
