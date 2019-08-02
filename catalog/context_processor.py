from .models import Category

def categories(request):
    cats = Category.objects.all()[:12]
    result = {'categories': cats}
    return result