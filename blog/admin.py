from django.contrib import admin
from .models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Register Post model to Admin panel and define fields which will
    use summernote editor as well as customize admin panel.
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
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', )
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
        # Iterates  over selected queryset of comments and check if
        # comment is approved
        for comment in queryset:
            if not comment.approved:
                comment.approved = True
                comment.save()
                # Increment the comment_counter field of the associated post
                post = comment.post
                post.comment_counter += 1
                post.save()
