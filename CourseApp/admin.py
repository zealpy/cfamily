from django.contrib import admin, messages

from CourseApp.models import Course
from django.utils.html import format_html

from inline_actions.admin import InlineActionsModelAdminMixin
from inline_actions.actions import ViewAction, DeleteAction
from django.utils.translation import ugettext_lazy as _


class DoInactiveActionsMixin(object):
    def get_inline_actions(self, request, obj=None):
        actions = super(DoInactiveActionsMixin, self).get_inline_actions(request, obj)
        if obj:
            if obj.status == Course.a:
                actions.append('inactivate')
            elif obj.status == Course.i:
                actions.append('activate')
        return actions

    def inactivate(self, request, obj, parent_obj=None):
        obj.status = Course.i
        obj.save()
        messages.info(request, _("Status Inactive."))
    inactivate.short_description = _("Active")

    def activate(self, request, obj, parent_obj=None):
        obj.status = Course.a
        obj.save()
        messages.info(request, _("Status Active."))
    activate.short_description = _("Inactive")

@admin.register(Course)
class CourseAdmin(DoInactiveActionsMixin,ViewAction,DeleteAction,InlineActionsModelAdminMixin,admin.ModelAdmin):
    #pass
    list_display = ('name', 'category', 'no_of_class', 'faculty_name')
