from django.contrib import admin, messages

from Course.models import Course, Topic, TopicVideo, DiscountCoupon
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


class InLineTopic(admin.TabularInline):
    extra = 1
    model = Topic

class InLineCoupon(admin.TabularInline):
    max_num = 1
    model = DiscountCoupon

@admin.register(Course)
class CourseAdmin(DoInactiveActionsMixin,ViewAction,InlineActionsModelAdminMixin,admin.ModelAdmin):
    inlines = [InLineTopic, InLineCoupon]

    """
    fieldsets = (
        (None, {
            'fields': (
                'name','category','faculty_name'
            )
        }),
    )
    """
    list_display = ('name', 'category', 'no_of_class', 'faculty_name', 'image_tag')

class InLineTopicVideo(admin.TabularInline):
    model = TopicVideo

@admin.register(Topic)
class TopicAdmin(DoInactiveActionsMixin,ViewAction,InlineActionsModelAdminMixin,admin.ModelAdmin):
    inlines = [InLineTopicVideo]

@admin.register(TopicVideo)
class TopicVideoAdmin(DoInactiveActionsMixin,ViewAction,InlineActionsModelAdminMixin,admin.ModelAdmin):
    pass

@admin.register(DiscountCoupon)
class DiscountCouponAdmin(DoInactiveActionsMixin,ViewAction,InlineActionsModelAdminMixin,admin.ModelAdmin):
    pass
    """
    fieldsets = (
        (None, {
            'fields': (
                'discount', 'status', 'start_date', 'end_date'
            )
        }),
    )
    """


