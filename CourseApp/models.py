import os

from django.db import models
from django.utils.translation import ugettext_lazy as _

from CFamily.settings import MEDIA_ROOT, BASE_DIR, MEDIA_URL
from CategoryApp.models import Category
from CategoryApp.utils import get_unique_slug

class Course(models.Model):
    a = 'Active'
    i = 'Inactive'
    f = 'Free'
    p = 'Paid'

    STATUS_CHOICES = (
        (a, _("Active")),
        (i, _("Inactive")),
    )
    COURSE_CHOICES = (
        (f, _("Free")),
        (p, _("Paid")),
    )
    upload = os.path.join(MEDIA_ROOT.strip("/"), 'upload')
    print("-->"+upload)
    category = models.ForeignKey(Category, null=True, related_name='child', on_delete=models.CASCADE)
    name = models.CharField('Title', max_length=120)
    slug = models.SlugField(blank=True, unique=True, max_length=100)
    faculty_name = models.CharField(max_length=50)
    course_image = models.ImageField(upload_to = 'upload/')
    no_of_class = models.IntegerField('Number of Classes', blank=True, null=True)
    course_detail = models.TextField('Detail')
    course_type = models.CharField(max_length=10, choices=COURSE_CHOICES, default=f)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=a)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'name', 'slug')
        super().save(*args, **kwargs)