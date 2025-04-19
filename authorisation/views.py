from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        email = request.POST['email'].replace(' ','').lower()
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)
        if user:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('register')


    return render(request, 'authorisation/login.html')



def register(request):

    if request.method == 'POST':
        email = request.POST['email'].replace(' ','').lower()
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'A user with this email already exists')
            return redirect('register')


        newUser = User.objects.create_user(email=email,username=email,password=password2)
        newUser.save()

        auth.login(request, newUser)
        return redirect('home')

    return render(request, 'authorisation/register.html')