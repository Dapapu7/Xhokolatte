from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

<<<<<<< Updated upstream
    path('', include('XhocolatteApp.urls', namespace='xhocolatte')),
=======
    path('', include('XhocolatteApp.urls')),
    path('blog/', include('XhocolatteBlog.urls', namespace='blog')),
>>>>>>> Stashed changes
    path('carrito/', include('basket.urls', namespace='basket')),
    path('accounts/', include('account.urls', namespace='account')),
    path('checkout/', include('checkout.urls', namespace='checkout')),
    path('orders/', include('checkout.urls', namespace='checkout')),
    path('', include('django.contrib.auth.urls')),
]
