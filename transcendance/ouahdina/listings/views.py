from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands':bands})

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons la vie !</p>')


def index(request):
    return HttpResponse("Welcome to the users section!")

from django.http import HttpResponseRedirect
import urllib.parse

CLIENT_ID = 'ton_client_id'
REDIRECT_URI = 'http://127.0.0.1:8000/api/auth/callback/'

def intra42_login(request):
    base_url = "https://api.intra.42.fr/oauth/authorize"
    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
    }
    url = f"{base_url}?{urllib.parse.urlencode(params)}"
    return HttpResponseRedirect(url)
