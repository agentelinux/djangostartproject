"""appaula1 URL Configuration

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
from django.urls import path, re_path
from appaula1 import views
from artigo import views as artigos


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('artigo', artigos.listar, name="artigos"),

    path('home', views.home, name="homepage"),
    path('blog-post-list', views.post_list, name="lista de posts"),
    re_path('^blog/(?P<postid>[\w|\W]+)/', views.blog, name="blogpage"),
    re_path('', views.pages, name="curinga"),

] 
