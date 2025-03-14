from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.

#home
#login page
#registration page

def home(request):
    return render(request, 'home.html')

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():

            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        user = authenticate(username=username, password=password)


        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/home/')
    return render(request, 'login.html')

def registrationPage(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Username already taken!")
            return redirect('/register/')

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )

        user.set_password(password)
        user.save()
        messages.info(request, "Account created Successfully!")
        return redirect('/register/')

    return render(request, 'register.html')