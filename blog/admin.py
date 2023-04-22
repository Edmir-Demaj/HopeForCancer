from django.contrib import admin
from . import models
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Define fields which will use summernote editor in admin panel
    and customize this admin panel.
    """

    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "category", "author", "created_date", "status")
    search_fields = ["title", "author__username", "category__category_name"]
    list_filter = ("category__category_name", "status", "created_date")
    summernote_fields = "content"
