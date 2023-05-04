from . import views
from django.urls import path


urlpatterns = [
    path('', views.BlogPage.as_view(), name='blog_page'),
    path('<slug:slug>/', views.postDetail, name='post_detail'),
    path('create_post', views.CreatePost.as_view(), name='create_post'),
]
