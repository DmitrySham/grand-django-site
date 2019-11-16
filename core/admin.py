from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist

from adminsortable2.admin import SortableAdminMixin
from .models import *


# Register your models here.

@admin.register(Slider)
class SliderAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'title', 'is_active', 'order_index']
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

    fieldsets = (
        (None, {'fields': (
            'footer_description',
            'header_phone',
            'header_email',
        )}),

        ('Страница: Главная', {'fields': (
            # 'index_page_text',

            'why_choose_us',
            # 'schedule',
            # 'schedule_thumbnail',
            # 'schedule_list_items',
            #
            # 'grand_service',
            # 'grand_service_thumbnail',
            # 'grand_service_list_items',
            #
            # 'grand_smeta',
            # 'grand_smeta_thumbnail',
            # 'grand_smeta_list_items',

            'icon_heading',
            'icon_1c',
            'icon_online_cashbox',
            'icon_schedule',
            'icon_grand_smeta',
            'icon_electronic_sign',
            'icon_certificates',
        )}),

        ('Страница: Гранд Смета', {'fields': (
            'grand_smeta_text',
            'grand_smeta_header_image'
        )}),

        ('Страница: Новости', {'fields': (
            'news_header_image',
        )}),

        ('Страница: Учебный центр', {'fields': (
            'schedule_header_image',
        )}),

        ('Страница: 1С', {'fields': (
            'one_c_header_image',
        )}),

        ('Страница: Онлайн кассы', {'fields': (
            'online_cash_box_header_image',
        )}),

        ('Страница: Элек. подписи', {'fields': (
            'electronic_signature_header_image',
        )}),
    )

    inlines = (SocialProfileLinksStackedInline, FooterMenuLinksStackedInline)

    def has_add_permission(self, request):
        return self.model.objects.count() < 1


@admin.register(GrandSmeta)
class GrandSmeta(admin.ModelAdmin):
    list_display = ['title', 'price']
    search_fields = ['title', 'description', 'full_description']

    prepopulated_fields = {'slug': ('title',)}


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return self.model.objects.count() < 1


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'is_read', 'is_reacted', 'created_at']
    list_filter = ['is_read', 'is_reacted', 'created_at']

    readonly_fields = ['is_read', 'created_at', 'name', 'subject', 'email', 'message']

    def has_add_permission(self, request):
        return False

    def change_view(self, request, object_id, form_url='', extra_context=None):
        try:
            feedback_object = Feedback.objects.get(id=object_id)
            if not feedback_object.is_read:
                feedback_object.is_read = True
                feedback_object.save()
        except ObjectDoesNotExist:
            pass

        return super(FeedbackAdmin, self).change_view(request, object_id, form_url=form_url, extra_context=extra_context)
