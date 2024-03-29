"""Cfamily URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.urls import path, include

#from Category.views import category_delete_view
from Cfamily import settings
from . import views

admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.site_title = "Cfamily Admin"
admin.site.index_title = "Welcome to Cfamily"

urlpatterns = [
    #path('category/<int:id>/delete/', category_delete_view, name='category_delete')
    #path('', views.index, name='index'),
    #path('home', views.home, name='home'),
    #url(r'^category/(?P<hierarchy>.+)/$', views.show_category, name='category'),
]
