from . import views
from django.urls import path


urlpatterns = [
    path('', views.BlogPage.as_view(), name='blog_page'),
    path('post_detail/<slug:slug>/', views.postDetail, name='post_detail'),
    path('create_post/', views.CreatePost.as_view(), name='create-post'),
    path('update_post/<slug:slug>/', views.update_post, name='update-post'),
    path(
        "delete_post/<slug:slug>/",
        views.DeletePost.as_view(),
        name="delete-post",
    ),
]
