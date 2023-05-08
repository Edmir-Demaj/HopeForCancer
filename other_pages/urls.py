from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_page, name='about'),
    path('cancer_info/', views.cancer_info_page, name='cancer-info'),
]
