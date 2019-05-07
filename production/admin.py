from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(OneC)
class OneCAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'short_description', 'full_description']


@admin.register(OnlineCashbox)
class OnlineCashboxAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'short_description', 'full_description']
