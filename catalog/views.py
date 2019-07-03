from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    response = render(request, 'index.html')
    return response


def catalog(request):
    response = render(request, 'catalog.html')
    return response
