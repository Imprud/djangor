from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.http import HttpResponse
from .models import Category, Agency
from django.db.models import Count


def index(request):

    category = Category.objects.get(slug='mobile-app-development')
    companies = category.agency_set.all()[:12]

    context = {
        'companies': companies,
    }
    response = render(request, 'index.html', context)

    return response


def all_cats(request):
    all_cats = Category.objects.annotate(
        agency_count=Count('agency')).order_by('-agency_count')

    context = {
        'all_cats': all_cats
    }
    response = render(request, 'categories.html', context)
    return response



def catalog(request, **kwargs):
    slug = kwargs.get('slug', None)
    if not slug:
        return HttpResponseBadRequest()

    category = Category.objects.get(slug=slug)

    employees = request.GET.get('employees', None)
    rates = request.GET.get('rate', None)

    if employees:
        companies = category.agency_set.filter(employees=employees)[:30]
    elif rates:
        companies = category.agency_set.filter(rates=rates)[:30]
    else:
        companies = category.agency_set.all()[:30]

    rates_list = category.agency_set.all().values('rates').distinct()
    employees_num = category.agency_set.all().values('employees').distinct()


    context = {
        'companies': companies,
        'main_cat': category,
        'employees_num': employees_num,
        'rates_list': rates_list,
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


