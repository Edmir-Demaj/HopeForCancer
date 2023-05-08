from django.contrib import admin
from .models import Value
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Value)
class ValueAdmin(SummernoteModelAdmin):
    """
    Define which field will use summernote editor in admin panel
    and customize this admin panel for Value model.
    """
    list_display = ('title', 'content')
    search_fields = ('title', 'content')
    summernote_fields = 'content'
