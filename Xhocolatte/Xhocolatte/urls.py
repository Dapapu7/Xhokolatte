from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),


    path('', include('XhocolatteApp.urls', namespace='xhocolatte')),
    path('blog/', include('XhocolatteBlog.urls', namespace='blog')),
    path('carrito/', include('basket.urls', namespace='basket')),
    path('accounts/', include('account.urls', namespace='account')),
    path('checkout/', include('checkout.urls', namespace='checkout')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('', include('django.contrib.auth.urls')),
]
