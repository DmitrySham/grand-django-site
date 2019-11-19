from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['get_truncated_title', 'created_at', 'is_active']

    list_filter = ['created_at', 'is_active']
    search_fields = ['title', 'short_description', 'full_description', 'slug']

    prepopulated_fields = {'slug': ('title',)}

    readonly_fields = ['created_at']

    fieldsets = (
        ('Общее', {'fields': (
            'is_active',
            'thumbnail',
            'atr_alt',
            'title',
            'slug',
            'short_description',
            'content',
            'created_at',
        )}),
        ('SEO', {'fields': (
            'page_title',
            'page_meta_keywords',
            'page_meta_description',
            'page_meta_og_title',
            'page_meta_og_description',
            'page_meta_og_image',
        )})
    )
