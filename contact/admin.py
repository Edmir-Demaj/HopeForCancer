from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):
    """
    Register Contact model to admin page and customize this panel.
    """
    list_display = ('name', 'email', 'subject')
    search_fields = ['name', 'email', 'subject']
    summernote_fields = 'content'


@admin.register(FAQ)
class FaqAdmin(SummernoteModelAdmin):
    """
    Register FAQ model in admin panel and customize this panel.
    """
    list_display = ('title', 'content')
    search_fields = ['title']
    summernote_fields = 'content'
