from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_page, name='about'),
    path('info/', views.info_page, name='info'),
    path('my-view/', views.my_view, name='my-view'),
]
