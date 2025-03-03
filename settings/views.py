from django.shortcuts import render
from .forms import CardForm
from django.http import HttpResponse

# Create your views here.
def render_card(request: HttpResponse):
    form = CardForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            form.save()

    return render(request, 'card.html', context={'form': form})

def render_settings(request: HttpResponse):
    return render(request, 'settings.html')