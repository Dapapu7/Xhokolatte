from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
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

def add_blog(request):
    context = {'form' : BlogForm}
    if request.method == 'POST':
        form = BlogForm(request.POST)
        image = request.FILE['image']
        title = request.POST.get('tile')
        user = request.user

        if form.is_valid():
            content = form.cleaned_data['content']

        blog_obj = BlogModel.objets.create(
            user = user , title = title,
            content = content , image = image
        )
        print(blog_obj)
        return redirect('/add_blog/')

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

    

