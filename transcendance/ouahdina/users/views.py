from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connecte automatiquement après inscription
            return HttpResponse("Enregistrement Réussi")  # Redirige vers une page d'accueil
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


from django.middleware.csrf import get_token

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponse("Connexion réussie")
    else:
        form = AuthenticationForm()

    try:
        with open('/mnt/c/ayael-ou/42project/test/transcendance/ouahdina/users/templates/users/login.html', 'r') as file:
            html_content = file.read()
    except FileNotFoundError:
        return HttpResponse("Fichier HTML introuvable.", status=404)

    csrf_token = get_token(request)
    html_content = html_content.replace('{{ csrf_token }}', csrf_token)
    html_content = html_content.replace('{{ form }}', ''.join([str(field) for field in form]))

    return HttpResponse(html_content)


def index(request):
    return HttpResponse("Welcome to the Users section!")