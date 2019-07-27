from django.contrib import admin
from .models import *
from adminsortable2.admin import SortableAdminMixin

# Register your models here.


@admin.register(OneC)
class OneCAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'price', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'short_description', 'full_description']


@admin.register(OnlineCashbox)
class OnlineCashboxAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'short_description', 'full_description']


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
