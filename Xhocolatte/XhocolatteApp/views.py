from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from django.core.mail import send_mail

from XhocolatteApp.models import Product

# Create your views here.

def  home(request):
    return render(request, 'XhocolatteApp/home.html')

def  privacidad(request):
    return render(request, 'XhocolatteApp/politicasPrivacidad.html')

def  productos(request):
    products = Product.objects.all()
    return render(request, 'XhocolatteApp/productos/productos.html', {'products': products})

def detalle_productos(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, 'XhocolatteApp/productos/detail.html', {'product': product})

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


    

