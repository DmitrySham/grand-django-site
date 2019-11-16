from django.contrib import admin
from .models import *
from adminsortable2.admin import SortableAdminMixin

# Register your models here.


class OneCImageInline(admin.TabularInline):
    model = OneCImage
    extra = 1


@admin.register(OneC)
class OneCAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'short_description', 'full_description']

    inlines = (OneCImageInline,)

    fieldsets = (
        ('Общее', {'fields': (
            'is_active',
            'title',
            'short_description',
            'full_description',
            'thumbnail',
            'cover_image',
            'price_box',
            'share_links',
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


class OnlineCashboxImageInline(admin.TabularInline):
    model = OnlineCashboxImage
    extra = 1


@admin.register(OnlineCashbox)
class OnlineCashboxAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'short_description', 'full_description']

    inlines = (OnlineCashboxImageInline,)

    fieldsets = (
        ('Общее', {'fields': (
            'is_active',
            'title',
            'short_description',
            'full_description',
            'price_box',
            'thumbnail',
            'cover_image',
            'share_links',
            'category',
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


@admin.register(ElectronicSignature)
class ElectronicSignatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'short_description', 'full_description']

    prepopulated_fields = {'slug': ('title',)}


@admin.register(ShareLinks)
class ShareLinkAdmin(admin.ModelAdmin):
    pass


@admin.register(OnlineCashBoxPartner)
class CashboxPartner(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_filter = ['is_active']


@admin.register(OnlineCashboxCategory)
class CashboxCategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
