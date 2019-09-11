from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from django.views.generic import DetailView
#from categoryApp.models import Category
from django.views.generic import (DetailView, ListView)
from cfamily.settings import MAIN_CATEGORY

from category.models import Category
from Course.models import Course


# Create your views here.
class HomeView(ListView):
    template_name = 'home/home.html'
    # context_object_name = 'category_list'

    def get_queryset(self):
        return Category.objects.filter(status='Active').values('name', 'description', 'image', 'parent_id').order_by('name')

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['course_list'] = Course.objects.all().order_by('name').reverse()[:3]

        # Language Category for home page
        context['language_category'] = Category.objects.filter(
            status='Active', parent_id='1').values('name', 'description', 'image', 'parent_id').order_by('name')[:6]

        # Database Category for home page
        context['database_category'] = Category.objects.filter(
            status='Active', parent_id='8').values('name', 'description', 'image', 'parent_id').order_by('name')[:3]

        # Bigdata for home page
        context['bigdata_category'] = Category.objects.filter(
            status='Active', parent_id='12').values('name', 'description', 'image', 'parent_id').order_by('name')[:3]

        # print('context', context)
        return context

class CategoryView(View):

    def get(self, request, cat_name, *args, **kwargs):
        context = {}
        context['category_name'] = cat_name.capitalize()
        # print('path:', category_name)
        cat_id = MAIN_CATEGORY.get(cat_name, '')

        context['category'] = Category.objects.filter(status='Active', parent_id=cat_id).values('name', 'description',
                                                                                                'image',
                                                                                                'parent_id').order_by(
            'name')
        return render(request, "home/category.html", context=context)


class CourseView(ListView):

    def get(self, request, cat_name, *args, **kwargs):
        context = {'course_list':''}
        context['category_name'] = cat_name.capitalize()
        try:
            obj = Category.objects.get(name__icontains=cat_name)
            # print('id val:',obj.id)
            context['course_list'] = Course.objects.filter(category_id=obj.id).values('name', 'faculty_name', 'no_of_class',
                                                                                   'course_detail', 'course_type', 'image')
            print(type(context['course_list']))
            # print('len::',len(context['course']))
        except Category.DoesNotExist:
            # We have no object! Do something...
            pass

        return render(request, "home/course_list.html", context=context)


class VideoView(View):

    def get(self, request):
        context = {}

        return render(request, 'home/video.html', context)


