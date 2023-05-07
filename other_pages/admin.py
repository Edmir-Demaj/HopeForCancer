from django.contrib import admin
from .models import Value


@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured_image', 'content')
    search_fields = ('title', 'content')
