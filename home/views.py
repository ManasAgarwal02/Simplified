from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        if len(name) < 2 or len(email) < 6 or len(phone) < 10 or len(desc) < 5:
            messages.error(request, 'Please enter the valid query.')
        else:
            messages.success(request, 'Your query has been sent successfully.')
            my_contact = Contact(name=name, email=email, phone=phone, desc=desc)
            my_contact.save()
    return render(request, 'home/contact.html')


def handleSignup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        name = request.POST.get("name")
        email = request.POST.get("email")
        pass1 = request.POST.get("password")
        pass2 = request.POST.get("confirm-password")
        if pass1 != pass2:
            messages.error(request, "Password and confirm password are not matching!")
            return redirect('home')
        if len(username) > 10:
            messages.error(request, "Your username should be less then 10 characters.")
            return redirect('home')
        if not username.isalnum():
            messages.error(request, "Your username should be alpha numeric.")
            return redirect('home')

        user = User.objects.create_user(username=username, first_name=name, email=email, password=pass1)
        user.save()
        messages.success(request, f"Welcome! {user.username} to the Simplified world. Logint to grt extra benefits.")
        return render(request, 'home/home.html')


def handleLogin(request):
    if request.method == "POST":
        loginUsername = request.POST.get("login-username")
        loginpass = request.POST.get("login-password")
        user = authenticate(username=loginUsername, password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome! {user.username} to the Simplified world.")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('home')


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect('home')
