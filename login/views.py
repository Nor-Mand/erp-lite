from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Login
def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # try:
        #     username = User.objects.get(username=username)
        # except:
        #     messages.error(request,"User no found!")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password incorrect!')
    return render(request, 'idLogin.html')


# Logout
def logout_user(request):
    logout(request)
    return redirect('login')