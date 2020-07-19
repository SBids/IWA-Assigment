from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from .models import Blog


def home(request):
    return render(request, 'blog/index.html')


def list_blog(request):
    data = Blog.objects.all()
    context = {
        'data': data
    }
    return render(request, 'blog/list.html', context=context)
