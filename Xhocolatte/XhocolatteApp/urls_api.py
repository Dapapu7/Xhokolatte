from django.urls import path

from XhocolatteApp.views_api import LoginView
from XhocolatteApp.views_api import RegisterView
from .views_api import *


urlpatterns = [
    path('login/', LoginView),
    path('register/', RegisterView),



]