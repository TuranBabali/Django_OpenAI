from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

#Other AUTH imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


def anonymous_required(function=None, redirect_url=None):

    if not redirect_url:
        redirect_url = 'dashboard'
    actual_decorator = user_passes_test(
        lambda u: u.is_anonymous,
        login_url=redirect_url
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


@anonymous_required
def login(request):
    if request.method == 'POST':
        email = request.POST['email'].replace(' ','').lower()
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)
        if user:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('register')


    return render(request, 'authorisation/login.html')


@anonymous_required
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
        return redirect('dashboard')

    return render(request, 'authorisation/register.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')