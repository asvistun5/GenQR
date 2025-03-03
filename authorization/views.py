from django.shortcuts import render, redirect
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login
from reg.models import User

# Create your views here.
def render_auth(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        surname = request.POST.get('surname')
        password = request.POST.get('password')
        user = authenticate(request=request, username=username, surname=surname, password=password, is_auth= True)
        if user:
            login(request=request, user=user)
        else:
            context = {"error": True}
        return redirect('/')
    return render(request, 'auth.html', context=context)