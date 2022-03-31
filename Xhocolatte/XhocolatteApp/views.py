from django.shortcuts import render, HttpResponse

# Create your views here.

def  home(request):
    return render(request, 'XhocolatteApp/home.html')

def  productos(request):
    return render(request, 'XhocolatteApp/productos.html')


def  contacto(request):
    return render(request, 'XhocolatteApp/contacto.html')

def blog(request):
    return render(request, 'XhocolatteApp/blog.html')

# def sign_up(request):



    

