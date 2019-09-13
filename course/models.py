import os
import uuid

from django.db import models
from django.utils.deconstruct import deconstructible
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from category.models import Category
from category.utils import get_unique_slug
from Cfamily.settings import MEDIA_ROOT


class Course(models.Model):
    a, i, f, p = 'Active', 'Inactive', 'Free', 'Paid'
    STATUS_CHOICES = (
        (a, _("Active")),(i, _("Inactive")),
    )
    COURSE_CHOICES = (
        (f, _("Free")),(p, _("Paid")),
    )

    category = models.ForeignKey(Category, null=True, related_name='child', on_delete=models.CASCADE)
    name = models.CharField('Title', unique=True, max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    faculty_name = models.CharField(max_length=50)
    no_of_class = models.IntegerField('Number of Classes', blank=True, null=True)
    course_detail = models.TextField('Detail')
    course_type = models.CharField(max_length=10, choices=COURSE_CHOICES, default=f)

    @deconstructible
    class PathAndRename(object):
        def __init__(self, sub_path):
            self.path = sub_path

        def __call__(self, instance, filename):
            ext = filename.split('.')[-1]  # eg: 'jpg'
            new_name = '{}.{}'.format(uuid.uuid4().hex, ext)
            return os.path.join(self.path, new_name)

    image = models.ImageField(upload_to=PathAndRename('upload/category/course/'))
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=a)
    meta_title = models.CharField(max_length=100, blank=True)
    meta_keyword = models.CharField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'course'

    def __str__(self):
        return self.name

    def image_tag(self):
        if self.image:
            head, tail = os.path.split(MEDIA_ROOT)
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' %  (head + self.image.url))
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    @property
    def topics(self):
        return self.topics_set.all().order_by('created')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'name', 'slug')
        super().save(*args, **kwargs)

class Topic(models.Model):
    a, i = 'Active', 'Inactive'
    STATUS_CHOICES = (
        (a, _("Active")), (i, _("Inactive")),
    )
    course = models.ForeignKey(Course, null=True, related_name='topicchild', on_delete=models.CASCADE)
    name = models.CharField('Title', unique=True, max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=a)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TopicVideo(models.Model):
    a, i = 'Active', 'Inactive'
    STATUS_CHOICES = (
        (a, _("Active")), (i, _("Inactive")),
    )

    #course = models.ForeignKey(course, null=True, related_name='videochild', on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, null=True, related_name='topchild', on_delete=models.CASCADE)
    name = models.CharField('Title', unique=True, max_length=255)
    video = models.FileField(upload_to='upload/category/course/topic/')
    free = models.BooleanField(_('free'), default=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=a)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class DiscountCoupon(models.Model):
    a, i = 'Active', 'Inactive'
    STATUS_CHOICES = (
        (a, _("Active")), (i, _("Inactive")),
    )
    A, B, C, D = '25', '50', '75', '100'
    DISCOUNT_CHOICES = (
        (A, _("25")),(B, _("50")),(C, _("75")),(D, _("100")),
    )
    course = models.ForeignKey(Course, null=True, related_name='discountchild', on_delete=models.CASCADE)
    discount = models.CharField(max_length=10, choices=DISCOUNT_CHOICES, blank=True)
    coupon = models.CharField(max_length=10, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=a)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.discount