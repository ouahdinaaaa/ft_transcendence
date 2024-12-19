from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from listings.models import AddUserFirst  # Importer le modèle utilisateur personnalisé
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponse("Connexion réussie")
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})

def index(request):
    return HttpResponse("Welcome to the Users section!")
