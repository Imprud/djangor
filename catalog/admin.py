from django.contrib import admin
from .models import Category, Review, Agency


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    fields = ['name', 'slug']


class AgencyAdmin(admin.ModelAdmin):
    list_filter = ['cats']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Review)
admin.site.register(Agency, AgencyAdmin)
