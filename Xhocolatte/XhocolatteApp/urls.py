from django.urls import path

from XhocolatteApp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "xhocolatte"

urlpatterns = [
    path('', views.home, name = "Home"),

    path('productos/', views.productos, name = "Productos"),
    path('productos/<slug:slug>', views.detalle_productos, name='detalle_productos'),
     
    path('contacto/', views.contacto, name = "Contacto"),

    path('politicasPrivacidad/', views.privacidad, name = "Politicas"),
    path('contactar/', views.contactar, name = "contactar"),
] 

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)