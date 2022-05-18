from django.shortcuts import render

from XhocolatteBlog.models import BlogModel

# Create your views here.
def  blog(request):
    context = {'blogs' : BlogModel.objects.all()}
    return render(request, 'XhocolatteApp/blog.html', context)

