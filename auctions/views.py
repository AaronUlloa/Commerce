from django.shortcuts import render
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from .models import User, Bid, Category, Listing, Comment

# Create your views here.
def index(request):
    activeListings = Listing.objects.filter(isActive=True)
    allCategory = Category.objects.all()
    return render(request, "view/index.html", {
        "title": "Publicaciones Activas",
        "listings": activeListings,
        "categories": allCategory
    })

def showCategories(request):
    activeListings = Listing.objects.filter(isActive=True)
    if activeListings:
        return render(request, "auctions/index.html", {
            "title": "Categories",
            "categories": Category.objects.all(),
            "listings": activeListings
        })
    else:
        return render(request, "auctions/index.html", {
            "title": "Categories",
            "categories": Category.objects.all(),
            "message": "No Listing"
        })

def addNew(request):
    if request.method == "GET":
        allCategories = Category.objects.all()
        return render(request, "view/addArticulo.html",{
            "title": "Publica Tu Articulo",
            "categories": allCategories
        })
    else:
        # Obteniendo la data del formulario
        title = request.POST["title"]
        description = request.POST["description"]
        image1 = request.POST["image1"]
        image2 = request.POST["image2"]
        image3 = request.POST["image3"]
        price = request.POST["price"]
        category = request.POST["category"]
        # Obteniendo la categoria escogida
        categoryData = Category.objects.get(categoryName = category)
        # Obteniendo el precio
        # priceData = Bid.objects.get(bid = price)
        # Usuario Actual
        currenUser = request.user
        # Creando la nueva publicacion
        newListing = Listing(
                title=title,
                image1=image1,
                image2=image2,
                image3=image3,
                description=description,
                category=categoryData,
                price=price,
                owner=currenUser
                )
        # Guardando la publicacion
        newListing.save()
        # Retornamos al index
        return HttpResponseRedirect(reverse("auctions:index"))
        




def forget(request):
    return render(request, "auth/forget.html", {"title": "Recuperar cuenta en AuctionsLess"})




def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("auctions:index"))
        else:
            return render(request, "auth/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auth/login.html",{
            "title": "Ingresa ahora en BidHub"
            })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("auctions:index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auth/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auth/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("auctions:index"))
    else:
        return render(request, "auth/register.html", {
            "title": "Registrate ahora en BidHub"
            })
