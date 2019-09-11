#core file imports
from tinymce.models import HTMLField
from .utils import get_unique_slug

#django imports
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import truncatechars

from cfamily import settings

class Category(models.Model):

    a='Active'
    i='Inactive'

    STATUS_CHOICES = (
        (a, _("Active")),
        (i, _("Inactive")),
    )

    parent = models.ForeignKey('self',blank=True, null=True, related_name='children',on_delete=models.CASCADE)  # on_delete=DO_NOTHING
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='upload/category/')
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default=a)
    meta_title = models.CharField(max_length=255,unique=True, blank=True)
    meta_keyword = models.CharField(max_length=255,blank=True)
    meta_descrition = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    @property
    def short_description(self):
        return truncatechars(self.description, 100)

    class Meta:
        unique_together = ('meta_title', 'parent',)    #enforcing that there can not be two
        verbose_name_plural = "categories"       #categories under a parent with same slug
        db_table = 'category'

    """
    def save(self, *args, **kwargs):
        if not self.meta_title:
            self.meta_title = get_unique_slug(self, 'name', 'meta_title')
        super().save(*args, **kwargs)
    """


    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.name]                  # post.  use __unicode__ in place of       # __str__ if you are using python 2
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])

"""
class Post(models.Model):
    user =  models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    category = models.ForeignKey('category', null=True, blank=True, on_delete=models.CASCADE)
    content = HTMLField('Content')
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False,auto_now_add=False,)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_cat_list(self):           #for now ignore this instance method,
        k = self.category
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent

        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]
"""

"""
class User(AbstractUser):
    pass
"""








