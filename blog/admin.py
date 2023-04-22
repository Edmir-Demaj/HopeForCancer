from django.contrib import admin
from .models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Define fields which will use summernote editor in admin panel
    and customize this admin panel.
    """

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'author', 'created_date', 'status')
    search_fields = ['title', 'author__username', 'category__category_name']
    list_filter = ('category__category_name', 'status', 'created_date')
    summernote_fields = 'content'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Register Category model in admin panel and customize this panel.
    """
    list_display = ('category_name', 'slug')
    search_fields = ['category_name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Register Comment model in admin panel and customize this panel.
    """
    list_display = ('name', 'body', 'post', 'created_date', 'approved')
    search_fields = ['name', 'email', 'body']
    list_filter = ('created_date', 'approved')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        Approve comments by changing its default value to True
        """
        queryset.update(approved=True)
