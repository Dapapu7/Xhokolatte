from socket import IPPORT_RESERVED
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from XhocolatteApp.forms import RegisterForm
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def  home(request):
    return render(request, 'XhocolatteApp/home.html')

def  productos(request):
    return render(request, 'XhocolatteApp/productos.html')


def  contacto(request):
    return render(request, 'XhocolatteApp/contacto.html')

def contactar(request):
    if request.method == "POST":
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + " /Email: " + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["ogre811@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently = False)
        return render(request, "XhocolatteApp/contactoExitoso.html")
    return render(request, "XhocolatteApp/contacto.html")


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

    

