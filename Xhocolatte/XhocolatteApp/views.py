from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from XhocolatteApp.forms import RegisterForm

# Create your views here.

def  home(request):
    return render(request, 'XhocolatteApp/home.html')

def  productos(request):
    return render(request, 'XhocolatteApp/productos.html')


def  contacto(request):
    return render(request, 'XhocolatteApp/contacto.html')

def blog(request):
    return render(request, 'XhocolatteApp/blog.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    
    return render(request, 'registration/sign_up.html', {"form":form})

    

