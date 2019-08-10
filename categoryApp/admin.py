from django.contrib import admin, messages
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from .models import Category

from inline_actions.actions import DefaultActionsMixin, ViewAction, DeleteAction
from inline_actions.admin import InlineActionsMixin, InlineActionsModelAdminMixin

class DoInactiveActionsMixin(object):
    def get_inline_actions(self, request, obj=None):
        actions = super(DoInactiveActionsMixin, self).get_inline_actions(request, obj)
        if obj:
            if obj.status == Category.a:
                actions.append('inactivate')
            elif obj.status == Category.i:
                actions.append('activate')
        return actions

    def inactivate(self, request, obj, parent_obj=None):
        obj.status = Category.i
        obj.save()
        messages.info(request, _("Status Inactive."))
    inactivate.short_description = _("Inactivate")

    def activate(self, request, obj, parent_obj=None):
        obj.status = Category.a
        obj.save()
        messages.info(request, _("Status Active."))
    activate.short_description = _("Activate")

@admin.register(Category)
class CategoryAdmin(DoInactiveActionsMixin,ViewAction,DeleteAction,InlineActionsModelAdminMixin,admin.ModelAdmin):
#class CategoryAdmin(DoInactiveActionsMixin,ViewAction,InlineActionsModelAdminMixin,admin.ModelAdmin):
    def fullpath(self, obj):
        return format_html("{}->{}", obj.parent, obj.name)

    list_display = ('name','fullpath','description', 'status')

"""


class CategoryInline(DefaultActionsMixin,DoInactiveActionsMixin,InlineActionsMixin,admin.TabularInline):
    model = Category
    can_delete = True
    fields = ('name', 'status',)
    readonly_fields = ('name')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request):
        return True

class CategoryAdmin(admin.ModelAdmin):
    #...
    def naction(self, obj):
        return format_html("<a href='/admin/categoryApp/category/{}/change'>Edit/Delete</a>", obj.id)

    naction.short_description = "Action"

    def fullpath(self, obj):
        return format_html("{}->{}", obj.parent, obj.name)
    ...#

    list_display = ['name', 'fullpath', 'slug', 'description','status', 'naction']
    list_display_links = ['naction']
    search_fields = ['name', 'description']

admin.site.register(Category, CategoryAdmin)
--------------------------------------------------

"""
