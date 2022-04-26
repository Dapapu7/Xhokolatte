from django.urls import path

from XhocolatteApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = "Home"),

    path('productos/', views.productos, name = "Productos"),
    path('agregarProducto/<int:producto_id>/', views.agregar_producto, name = "Add"),
    path('eliminarProdcuto/<int:producto_id>/', views.eliminar_producto, name = "Del"),
    path('restarProdcuto/<int:producto_id>/', views.restar_producto, name = "Sub"),
    path('limpiarCarrito/', views.limpiar_carrito, name = "CLS"),
     
    path('contacto/', views.contacto, name = "Contacto"),
    path('blog/', views.blog, name = "Blog"),
    path('politicasPrivacidad/', views.privacidad, name = "Politicas"),
    path('sign-up/', views.sign_up, name = "sign_up"),
    path('contactar/', views.contactar, name = "contactar"),
] 

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)