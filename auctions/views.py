from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "view/index.html")


def login(request):
    return render(request, "auth/login.html", {"title": "Inicia Sesion en AuctionsLess"})


def register(request):
    return render(request, "auth/register.html", {"title": "Crea tu cuenta en AuctionsLess"})


def forget(request):
    return render(request, "auth/forget.html", {"title": "Recuperar cuenta en AuctionsLess"})
