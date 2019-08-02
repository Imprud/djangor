from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.http import HttpResponse
from .models import Category, Agency


def index(request):

    category = Category.objects.get(slug='mobile-app-development')
    companies = category.agency_set.all()[:12]

    context = {
        'companies': companies,
    }
    response = render(request, 'index.html', context)

    return response


def all_cats(request):
    context = {
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
        'companies': companies,
        'main_cat': category,
    }

    response = render(request, 'catalog.html', context)
    return response


def company(request, **kwargs):

    slug = kwargs.get('slug', None)

    if not slug:
        return HttpResponseBadRequest()

    company = Agency.objects.get(slug=slug)

    context = {
        'company': company.name,
        'logo': company.logo,
        'description': company.description,
        'rates': company.rates,
        'location': company.location,
        'year': company.year,
        'employees': company.employees,
        'services': company.services,
        'scores': company.scores,
        'email': company.email,
        'phone': company.phone,
        'address': company.address,
        'company_cats': company.cats.all()
    }


    response = render(request, 'company-single.html', context)
    return response


