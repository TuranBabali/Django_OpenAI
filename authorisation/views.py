from django.shortcuts import render


def login(request):
    return render(request, 'authorisation/login.html')

def register(request):
    return render(request, 'authorisation/register.html')