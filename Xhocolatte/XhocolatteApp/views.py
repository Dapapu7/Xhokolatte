from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from XhocolatteApp.Carrito import Carrito
from XhocolatteApp.forms import RegisterForm
from django.conf import settings
from django.core.mail import send_mail

from XhocolatteApp.models import Producto

# Create your views here.

def  home(request):
    return render(request, 'XhocolatteApp/home.html')

def  privacidad(request):
    return render(request, 'XhocolatteApp/politicasPrivacidad.html')

def  productos(request):
    productos = Producto.objects.all()
    return render(request, 'XhocolatteApp/productos.html', {'productos': productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = producto_id)

    carrito.agregar(producto)
    return redirect('Productos')

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = producto_id)

    carrito.eliminar(producto)
    return redirect('Productos')

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = producto_id)

    carrito.restar(producto)
    return redirect('Productos')

def limpiar_carrito(request):
    carrito = Carrito(request)

    carrito.limpiar()
    return redirect('Productos')


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

    

