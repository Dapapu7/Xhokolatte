from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('XhocolatteApp.urls')),
    path('carrito/', include('basket.urls', namespace='basket')),
    path('accounts/', include('account.urls', namespace='account')),
    path('checkout/', include('checkout.urls', namespace='checkout')),
    path('', include('django.contrib.auth.urls')),
]
