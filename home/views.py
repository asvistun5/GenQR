from django.shortcuts import render, redirect
from django.contrib.auth import logout


def render_home(request):
    if request.user:
        return render(request=request, template_name= "home.html") 
    else:
        return redirect("auth")

def logout_user(request):
    logout(request)
    return redirect('auth')