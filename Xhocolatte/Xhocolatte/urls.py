from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('XhocolatteApp.urls')),
    path('carrito/', include('basket.urls', namespace='basket')),
    path('', include('django.contrib.auth.urls')),
]
