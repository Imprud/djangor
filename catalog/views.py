from django.shortcuts import render
from django.http import HttpResponse
from .models import Category


def index(request):
    context = {
        'categories': Category.objects.all()[:12]
    }
    response = render(request, 'index.html', context)
    return response


def catalog(request):
    response = render(request, 'catalog.html')
    return response
