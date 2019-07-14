from django.contrib import admin
from .models import Category, Review, Agency
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    fields = ['name', 'slug']


class AgencyAdmin(SummernoteModelAdmin):
    list_display = ['name', 'show_image', 'slug']
    list_filter = ['cats']
    summernote_fields = ('description',)

    def show_image(self, obj):
        try:
            img = mark_safe(f'<img src="{obj.origin_image}">')
        except Exception:
            img = 'not found'
        return img


admin.site.register(Category, CategoryAdmin)
admin.site.register(Review)
admin.site.register(Agency, AgencyAdmin)
