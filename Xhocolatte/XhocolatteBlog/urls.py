
from django.urls import path, include
from .views import *
from XhocolatteBlog import views

app_name = 'blog'

urlpatterns = [
        path('', views.blog, name = "Blog"),
]