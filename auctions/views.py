from contextlib import redirect_stdout
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
import datetime
from .models import Image, Shop, Stock, User, Product, Brend, Type, Sex, Resist, Comment, Watchlist

class ByForm(forms.Form):
    sum =  forms.CharField(label = 'Количество')
    by = forms.BooleanField()
    
def index(request):
    return render(request, "auctions/index.html", {
        "Resists": Resist.objects.all().order_by('id'),
        "Brends": Brend.objects.all().order_by('brend'),
        "Types": Type.objects.all().order_by('type'),
        "Sex": Sex.objects.all().order_by('sex'),
        "Stock": Stock.objects.all()
    })

def all(request):
    if request.method == "POST":
        try:
            data = request.POST
            brends = data.getlist('brends')
            types = data.getlist('types')
            sex = data.getlist('sex')
            resists = data.getlist('resists')
            return render(request, "auctions/brend.html", {
                "Products": Product.objects.filter(pr_Brend__id__in=brends).filter(pr_Type__id__in=types).filter(pr_Sex__id__in=sex).filter(pr_Resist__id__in=resists).order_by('pr_Name'),
                "Shops": Shop.objects.all(),
                "Brends": Brend.objects.all().order_by('brend'),
                "Types": Type.objects.all().order_by('type'),
                "Sex": Sex.objects.all().order_by('sex'),
                "Resists": Resist.objects.all().order_by('id'),
            })
        except request.exceptions.RequestException:
            return 'Empty'
    else:
        return render(request, "auctions/brend.html", {
            "Products": Product.objects.all().order_by('pr_Name'),
            "Shops": Shop.objects.all(),
            "Brends": Brend.objects.all().order_by('brend'),
            "Types": Type.objects.all().order_by('type'),
            "Sex": Sex.objects.all().order_by('sex'),
            "Resists": Resist.objects.all().order_by('id'),
        })

def brend(request, brend_id):
    if request.method == "POST":
        try:
            data = request.POST
            brends = data.getlist('brends')
            types = data.getlist('types')
            sex = data.getlist('sex')
            resists = data.getlist('resists')
            return render(request, "auctions/brend.html", {
                "Products": Product.objects.filter(pr_Brend__id__in=brends).filter(pr_Type__id__in=types).filter(pr_Sex__id__in=sex).filter(pr_Resist__id__in=resists).order_by('pr_Name'),
                "Shops": Shop.objects.all(),
                "Brends": Brend.objects.all().order_by('brend'),
                "Types": Type.objects.all().order_by('type'),
                "Sex": Sex.objects.all().order_by('sex'),
                "Resists": Resist.objects.all().order_by('id'),
            })
        except request.exceptions.RequestException:
            return 'Empty'
    else:
        return render(request, "auctions/brend.html", {
            "Products": Product.objects.filter(pr_Brend=brend_id).order_by('pr_Name'),
            "Shops": Shop.objects.all(),
            "Brends": Brend.objects.all().order_by('brend'),
            "Types": Type.objects.all().order_by('type'),
            "Sex": Sex.objects.all().order_by('sex'),
            "Resists": Resist.objects.all().order_by('id'),
        })
        
def type(request, type_id):
    if request.method == "POST":
        try:
            data = request.POST
            brends = data.getlist('brends')
            types = data.getlist('types')
            sex = data.getlist('sex')
            resists = data.getlist('resists')
            return render(request, "auctions/brend.html", {
                "Products": Product.objects.filter(pr_Brend__id__in=brends).filter(pr_Type__id__in=types).filter(pr_Sex__id__in=sex).filter(pr_Resist__id__in=resists).order_by('pr_Name'),
                "Shops": Shop.objects.all(),
                "Brends": Brend.objects.all().order_by('brend'),
                "Types": Type.objects.all().order_by('type'),
                "Sex": Sex.objects.all().order_by('sex'),
                "Resists": Resist.objects.all().order_by('id'),
            })
        except request.exceptions.RequestException:
            return 'Empty'
    else:
        return render(request, "auctions/brend.html", {
            "Products": Product.objects.filter(pr_Type=type_id).order_by('pr_Name'),
            "Shops": Shop.objects.all(),
            "Brends": Brend.objects.all().order_by('brend'),
            "Types": Type.objects.all().order_by('type'),
            "Sex": Sex.objects.all().order_by('sex'),
            "Resists": Resist.objects.all().order_by('id'),
        })

def sex(request, sex_id):
    if request.method == "POST":
        try:
            data = request.POST
            brends = data.getlist('brends')
            types = data.getlist('types')
            sex = data.getlist('sex')
            resists = data.getlist('resists')
            return render(request, "auctions/brend.html", {
                "Products": Product.objects.filter(pr_Brend__id__in=brends).filter(pr_Type__id__in=types).filter(pr_Sex__id__in=sex).filter(pr_Resist__id__in=resists).order_by('pr_Name'),
                "Shops": Shop.objects.all(),
                "Brends": Brend.objects.all().order_by('brend'),
                "Types": Type.objects.all().order_by('type'),
                "Sex": Sex.objects.all().order_by('sex'),
                "Resists": Resist.objects.all().order_by('id'),
            })
        except request.exceptions.RequestException:
            return 'Empty'
    else:
        return render(request, "auctions/brend.html", {
            "Products": Product.objects.filter(pr_Sex=sex_id).order_by('pr_Name'),
            "Shops": Shop.objects.all(),
            "Brends": Brend.objects.all().order_by('brend'),
            "Types": Type.objects.all().order_by('type'),
            "Sex": Sex.objects.all().order_by('sex'),
            "Resists": Resist.objects.all().order_by('id'),
        })

def resist(request, resist_id):
    if request.method == "POST":
        try:
            data = request.POST
            brends = data.getlist('brends')
            types = data.getlist('types')
            sex = data.getlist('sex')
            resists = data.getlist('resists')
            return render(request, "auctions/brend.html", {
                "Products": Product.objects.filter(pr_Brend__id__in=brends).filter(pr_Type__id__in=types).filter(pr_Sex__id__in=sex).filter(pr_Resist__id__in=resists).order_by('pr_Name'),
                "Shops": Shop.objects.all(),
                "Brends": Brend.objects.all().order_by('brend'),
                "Types": Type.objects.all().order_by('type'),
                "Sex": Sex.objects.all().order_by('sex'),
                "Resists": Resist.objects.all().order_by('id'),
            })
        except request.exceptions.RequestException:
            return 'Empty'
    else:
        return render(request, "auctions/brend.html", {
            "Products": Product.objects.filter(pr_Resist=resist_id).order_by('pr_Name'),
            "Shops": Shop.objects.all(),
            "Brends": Brend.objects.all().order_by('brend'),
            "Types": Type.objects.all().order_by('type'),
            "Sex": Sex.objects.all().order_by('sex'),
            "Resists": Resist.objects.all().order_by('id'),
        })

def details(request, Product_id):
    current_Product = Product.objects.get(id=Product_id)
    current_Shop = Shop.objects.get(sh_Product=current_Product)

    if request.method == "POST" and "by_Product" in request.POST:
        form = ByForm(request.POST)

        if form.is_valid():
            sum = int(form.cleaned_data['sum'])
            by = form.cleaned_data['by']
            current_Shop.sh_Left = current_Shop.sh_Total - current_Shop.sh_Sales
            if by==True and current_Shop.sh_Left-sum>=0:
                current_Shop.sh_Sales = current_Shop.sh_Sales + sum
                current_Shop.sh_Left = current_Shop.sh_Left - sum
                if current_Shop.sh_Left < 1:
                    current_Shop.sh_Status = False
                current_Shop.save()
                return HttpResponseRedirect(reverse("all"))
            else:
                return render(request, "auctions/detail.html", {
                    "Shops": Shop.objects.all(),
                    "Brends": Brend.objects.all().order_by('brend'),
                    "Types": Type.objects.all().order_by('type'),
                    "Sex": Sex.objects.all().order_by('sex'),
                    "Resists": Resist.objects.all().order_by('id'),
                    "comments": Comment.objects.all().filter(c_Product_id=Product_id).order_by('id'),
                    "current_Product": current_Product,
                    "current_Shop": current_Shop,
                    "Product_id": Product_id
                })
        else:
            return render(request, "auctions/detail.html", {
                    "Shops": Shop.objects.all(),
                    "Brends": Brend.objects.all().order_by('brend'),
                    "Types": Type.objects.all().order_by('type'),
                    "Sex": Sex.objects.all().order_by('sex'),
                    "Resists": Resist.objects.all().order_by('id'),
                    "comments": Comment.objects.all().filter(c_Product_id=Product_id).order_by('id'),
                    "current_Product": current_Product,
                    "current_Shop": current_Shop,
                    "Product_id": Product_id
            })
    elif request.method == "POST" and "addwatchlist" in request.POST:
        user_Id = request.POST['userid']
        watch_User = User.objects.get(id=user_Id)
        watch_Product_id = Product.objects.get(id=Product_id)
        watch_Shop = Shop.objects.get(sh_Product=watch_Product_id)
        watchlist = Watchlist.objects.create(wl_User=watch_User, wl_Product_id=watch_Product_id, wl_Shop=watch_Shop)
        watchlist.save()
        return render(request, "auctions/detail.html", {
            "Shops": Shop.objects.all(),
            "Brends": Brend.objects.all().order_by('brend'),
            "Types": Type.objects.all().order_by('type'),
            "Sex": Sex.objects.all().order_by('sex'),
            "Resists": Resist.objects.all().order_by('id'),
            "comments": Comment.objects.all().filter(c_Product_id=Product_id).order_by('id'),
            "current_Product": current_Product,
            "current_Shop": current_Shop
        })
        
    elif request.method == "POST" and "createcomment" in request.POST:
        user_Id = request.POST["userid"]
        comment_User = User.objects.get(id=user_Id)
        comment_Text = request.POST["commenttext"]
        comment_Date = datetime.datetime.now()
        new_Comment = Comment.objects.create(c_User=comment_User, c_Text=comment_Text, c_Date=comment_Date, c_Product_id=Product_id)
        new_Comment.save()
        return HttpResponseRedirect(reverse("details", args=(current_Product.id,)))

    else:
        return render(request, "auctions/detail.html", {
            "Shops": Shop.objects.all(),
            "Brends": Brend.objects.all().order_by('brend'),
            "Types": Type.objects.all().order_by('type'),
            "Sex": Sex.objects.all().order_by('sex'),
            "Resists": Resist.objects.all().order_by('id'),
            "comments": Comment.objects.filter(c_Product_id=Product_id).order_by('-id'),
            "current_Product": current_Product,
            "current_Shop": current_Shop
        })         

def watchlist(request, user_id):
    watch_User = User.objects.get(id=user_id)
    if request.method == "POST" and "delwatchlist" in request.POST:
        del_Watchlist = request.POST['delwatchlist']
        watchlist = Watchlist.objects.get(pk=del_Watchlist)
        watchlist.delete()
        return render(request, "auctions/watchlist.html", {
            "Shops": Shop.objects.all(),
            "Brends": Brend.objects.all().order_by('brend'),
            "Types": Type.objects.all().order_by('type'),
            "Sex": Sex.objects.all().order_by('sex'),
            "Resists": Resist.objects.all().order_by('id'),
            "Images": Image.objects.all(),
            "User": User.objects.all(),
            "Brend": Brend.objects.all(),
            "Watchlists": Watchlist.objects.filter(wl_User=watch_User).exclude(id=1)
        })
    elif request.method == "POST" and "watchlist" in request.POST:
        return render(request, "auctions/watchlist.html", {
            "Shops": Shop.objects.all(),
            "Brends": Brend.objects.all().order_by('brend'),
            "Types": Type.objects.all().order_by('type'),
            "Sex": Sex.objects.all().order_by('sex'),
            "Resists": Resist.objects.all().order_by('id'),
            "Images": Image.objects.all(),
            "User": User.objects.all(),
            "Brend": Brend.objects.all(),
            "Watchlists": Watchlist.objects.filter(wl_User=watch_User).exclude(id=1)
        })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
