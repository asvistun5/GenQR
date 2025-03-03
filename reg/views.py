from django.shortcuts import render, redirect
from django.db.utils import IntegrityError
from django.contrib.auth import login, logout
from .models import User


def render_reg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create(username= username, surname=surname, email=email, password= password)
        return redirect('auth')
    return render(request, 'reg.html')