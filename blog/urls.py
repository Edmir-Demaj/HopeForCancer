from . import views
from django.urls import path


urlpatterns = [
    path('', views.BlogPage.as_view(), name='blog_page'),
    path('post_detail/<slug:slug>/', views.postDetail, name='post_detail'),
    path('create_post/', views.CreatePost.as_view(), name='create-post'),
    path('update_post/<slug:slug>/', views.update_post, name='update-post'),
    path(
        'delete_post/<slug:slug>/',
        views.DeletePost.as_view(),
        name='delete-post',
    ),
    path(
        'like/<slug:slug>/',
        views.PostLike.as_view(),
        name='post_like',
    ),
    path('add_comment/<int:post_id>', views.add_comment, name='add_comment'),
    path(
        "edit_comment/<int:pk>",
        views.EditComment.as_view(),
        name="edit_comment",
    ),
]
