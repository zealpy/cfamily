"""cfamily URL Configuration

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

from django.contrib import admin
from django.urls import path, include

from home.views import HomeView, VideoView, CategoryView, CourseView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name="home_page"),
    path('video/', VideoView.as_view(), name="vdieo_page"),

    path('topic/<cat_name>/', CategoryView.as_view(), name='category_page'),
    path('<slug>/course/', CourseView.as_view(), name='course_page'),
    # path('')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "cFamily Computers Admin"
admin.site.site_title = "cFamily Computers Admin"
admin.site.index_title = "Welcome to cFamily Computers"
