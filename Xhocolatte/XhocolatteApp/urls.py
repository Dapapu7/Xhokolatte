from django.urls import path

from XhocolatteApp import views

urlpatterns = [
    path('', views.home, name = "Home"),
    path('productos/', views.productos, name = "Productos"),
    path('contacto/', views.contacto, name = "Contacto"),
    path('blog/', views.blog, name = "Blog"),
] 