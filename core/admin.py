from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'description', 'link']


@admin.register(AdminEmails)
class AdminEmailAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_active']
    search_fields = ['email']
    list_filter = ['is_active']


class SocialProfileLinksStackedInline(admin.StackedInline):
    model = SocialProfileLinks
    extra = 1


class FooterMenuLinksStackedInline(admin.StackedInline):
    model = FooterMenuLinks
    extra = 1


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):

    inlines = (SocialProfileLinksStackedInline, FooterMenuLinksStackedInline)

    def has_add_permission(self, request):
        return self.model.objects.count() < 1
