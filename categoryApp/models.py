from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

from cFamily import settings
from tinymce.models import HTMLField

class Category(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children',on_delete=models.CASCADE)  # on_delete=DO_NOTHING
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    status = models.CharField(max_length=10)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = ('slug', 'parent',)    #enforcing that there can not be two
        verbose_name_plural = "categories"       #categories under a parent with same slug

    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.name]                  # post.  use __unicode__ in place of                                                 # __str__ if you are using python 2
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])

class Post(models.Model):
    user =  models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
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


class User(AbstractUser):
    pass