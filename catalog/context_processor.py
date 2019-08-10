from .models import Category
from django.db.models import Count

def categories(request):

    cats = Category.objects.annotate(
        agency_count=Count('agency')).order_by('-agency_count')[:12]

    result = {'categories': cats}
    return result
