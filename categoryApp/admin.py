from django.contrib import admin
from django.utils.html import format_html

from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    #...
    def nstatus(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.status)

    nstatus.short_description = "Status"
    ...#

    list_display = ['name', 'parent', 'slug', 'nstatus']
    search_fields = ['name', 'slug']

admin.site.register(Category, CategoryAdmin)