from django.shortcuts import redirect, render, HttpResponse
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignupForm

# Create your views here.
def hello_world(request):
    all_products = Product.objects.all()
    return render(request, 'index.html', {'products': all_products})

def my_website(request):
    return HttpResponse("<p>Welcome to my website</p>")

def about(request):
    return render(request, "about.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Login successful."))
            return redirect("home")
        else:
            messages.error(request, ("Error in login."))
            return redirect("login")
    else:
        return render(request, "login.html")

def logout_user(request):
    logout(request)
    messages.success(request, ('Loging out is successful.'))
    return redirect("home")

def signup_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]

            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ('Your account is created.'))
            return redirect('home')
        else:
            messages.error(request, ('Error in sign up.'))
            return render(request, "signup.html", {'form': form})
    else:
        form = SignupForm()
    
    return render(request, "signup.html", {'form': form})

def product(request, pk):
    product = Product.objects.get(id=pk)

    return render(request, 'product.html', {'product': product})

def category(request, cat):
    cat = cat.replace('-',  '')
    try:
        category = Category.objects.get(name=cat)
        products = Product.objects.filter(category=category)

        return render(request, 'category.html', {'category': category, 'products': products})
    except:
        return redirect('home')