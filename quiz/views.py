from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenue sur la page d'accueil du site Handi A Dit !")
