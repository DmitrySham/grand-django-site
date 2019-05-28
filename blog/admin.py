from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['get_truncated_title', 'created_at', 'is_active']

    list_filter = ['created_at', 'is_active']
    search_fields = ['title', 'short_description', 'full_description', 'slug']

    prepopulated_fields = {'slug': ('title',)}
