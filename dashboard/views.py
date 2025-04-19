from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

#Other AUTH imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


@login_required
def home(request):
    context = {}
    return render(request,'dashboard/home.html',context)

