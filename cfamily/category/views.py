from django.shortcuts import render, get_object_or_404, redirect
from category.models import Category
#from category.models import Post

"""

def index(request):
    return render(request, 'home.html')
    
def home(request):
    return render(request, 'home.html')
    
"""
"""
def show_category(request,hierarchy= None):
    category_slug = hierarchy.split('/')
    category_queryset = list(category.objects.all())
    all_slugs = [ x.slug for x in category_queryset ]
    parent = None
    for slug in category_slug:
        if slug in all_slugs:
            parent = get_object_or_404(category,slug=slug,parent=parent)
        else:
            instance = get_object_or_404(Post, slug=slug)
            breadcrumbs_link = instance.get_cat_list()
            category_name = [' '.join(i.split('/')[-1].split('-')) for i in breadcrumbs_link]
            breadcrumbs = zip(breadcrumbs_link, category_name)
            return render(request, "postDetail.html", {'instance':instance,'breadcrumbs':breadcrumbs})

    return render(request,"categories.html",{'post_set':parent.post_set.all(),'sub_categories':parent.children.all()})

"""
"""
def category_delete_view(request, id):
    obj = get_object_or_404(category, id=id)
    if request.method == "Post":
        obj.delete()
        return redirect('../../')
    context = {"object":obj}
    return render(request, "category/category_delete.html", context)
"""



