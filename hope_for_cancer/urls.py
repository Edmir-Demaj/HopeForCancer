"""hope_for_cancer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

# Customize Header and Title on admin panel
admin.site.site_header = 'HopeForCancer'
admin.site.site_title = 'HopeForCancer'

# urls from other apps conected with project
urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('other_pages.urls'), name='home'),
    path('blog/', include('blog.urls'), name='blog_page'),
    path('', include('contact.urls')),
    path('accounts/', include('allauth.urls')),
]
