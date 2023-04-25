from . import views
from django.urls import path


urlpatterns = [
    path('', views.BlogPage.as_view(), name='blog_page'),
    path('<slug:slug>/', views.postDetail, name='post_detail'),
]
