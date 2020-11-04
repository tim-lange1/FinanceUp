from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST


@login_required
@require_POST
def index(request, username):
    return render(request, 'Stammdaten/base.html')

def home_view(request, username):
    return render(request, 'Stammdaten/home.html')
