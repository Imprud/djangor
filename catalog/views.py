from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.http import HttpResponse
from .models import Category


def index(request):
    context = {
        'categories': Category.objects.all()[:12]
    }
    response = render(request, 'index.html', context)
    return response


def all_cats(request):
    context = {
        'categories': Category.objects.all()[:12],
        'all_cats': Category.objects.all()
    }
    response = render(request, 'categories.html', context)
    return response



def catalog(request, **kwargs):
    slug = kwargs.get('slug', None)
    if not slug:
        return HttpResponseBadRequest()

    category = Category.objects.get(slug=slug)

    companies = category.agency_set.all()[:32]

    context = {
        'categories': Category.objects.all()[:12],
        'companies': companies,
        'main_cat': category
    }

    response = render(request, 'catalog.html', context)
    return response
