from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist

from adminsortable2.admin import SortableAdminMixin
from django.utils.safestring import mark_safe

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
            'index_page_h1_text',
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
            'one_c_h1_text',
            'one_c_header_image',
            'one_c_text',
        )}),

        ('Страница: Онлайн кассы', {'fields': (
            'online_cash_box_h1_text',
            'online_cash_box_header_image',
            'online_cash_box_text',
        )}),

        ('Страница: Элек. подписи', {'fields': (
            'electronic_signature_header_image',
        )}),

        ('Страница: Преподователи', {'fields': (
            'educators_h1_text',
            'educators_text',
        )})
    )

    inlines = (SocialProfileLinksStackedInline, FooterMenuLinksStackedInline)

    def has_add_permission(self, request):
        return self.model.objects.count() < 1


@admin.register(GrandSmeta)
class GrandSmeta(admin.ModelAdmin):
    list_display = ['title', 'price']
    search_fields = ['title', 'description', 'full_description']

    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        ('Общее', {'fields': (
            'is_active',
            'thumbnail',
            'art_alt',
            'title',
            'slug',
            'short_description',
            'description',
            'price',
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


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return self.model.objects.count() < 1


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'phone', 'is_read', 'is_reacted', 'created_at']
    list_filter = ['is_read', 'is_reacted', 'created_at']
    search_fields = ['name', 'subject', 'phone']

    readonly_fields = ['is_read', 'created_at', 'name', 'subject', 'phone', 'email', 'message']

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


@admin.register(Seo)
class SeoAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Главная страница', {'fields': (
            'index_page_title',
            'index_page_meta_keywords',
            'index_page_meta_description',
            'index_page_meta_og_title',
            'index_page_meta_og_description',
            'index_page_meta_og_image',
        )}),
        ('Новости (Каталог)', {'fields': (
            'blog_list_page_title',
            'blog_list_page_meta_keywords',
            'blog_list_page_meta_description',
            'blog_list_page_meta_og_title',
            'blog_list_page_meta_og_description',
            'blog_list_page_meta_og_image',
        )}),
        ('Гранд Смета (Каталог)', {'fields': (
            'grand_smeta_list_page_title',
            'grand_smeta_list_page_meta_keywords',
            'grand_smeta_list_page_meta_description',
            'grand_smeta_list_page_meta_og_title',
            'grand_smeta_list_page_meta_og_description',
            'grand_smeta_list_page_meta_og_image',
        )}),
        ('1C (Каталог)', {'fields': (
            'one_c_list_page_title',
            'one_c_list_page_meta_keywords',
            'one_c_list_page_meta_description',
            'one_c_list_page_meta_og_title',
            'one_c_list_page_meta_og_description',
            'one_c_list_page_meta_og_image',
        )}),
        ('Онлайн Кассы (Каталог)', {'fields': (
            'online_cashbox_list_page_title',
            'online_cashbox_list_page_meta_keywords',
            'online_cashbox_list_page_meta_description',
            'online_cashbox_list_page_meta_og_title',
            'online_cashbox_list_page_meta_og_description',
            'online_cashbox_list_page_meta_og_image',
        )}),
        ('Таблица с расписанием', {'fields': (
            'schedule_table_page_title',
            'schedule_table_page_meta_keywords',
            'schedule_table_page_meta_description',
            'schedule_table_page_meta_og_title',
            'schedule_table_page_meta_og_description',
            'schedule_table_page_meta_og_image',
        )}),
        ('Каталог курсов', {'fields': (
            'schedule_list_page_title',
            'schedule_list_page_meta_keywords',
            'schedule_list_page_meta_description',
            'schedule_list_page_meta_og_title',
            'schedule_list_page_meta_og_description',
            'schedule_list_page_meta_og_image',
        )}),
        ('Контакты', {'fields': (
            'contacts_page_title',
            'contacts_page_meta_keywords',
            'contacts_page_meta_description',
            'contacts_page_meta_og_title',
            'contacts_page_meta_og_description',
            'contacts_page_meta_og_image',
        )}),
        ('Лицензии', {'fields': (
            'licenses_page_title',
            'licenses_page_meta_keywords',
            'licenses_page_meta_description',
            'licenses_page_meta_og_title',
            'licenses_page_meta_og_description',
            'licenses_page_meta_og_image',
        )}),
        ('Преподователи', {'fields': (
            'educators_page_title',
            'educators_page_meta_keywords',
            'educators_page_meta_description',
            'educators_page_meta_og_title',
            'educators_page_meta_og_description',
            'educators_page_meta_og_image',
        )})
    )

    def has_add_permission(self, request):
        return self.model.objects.count() < 1


@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Общее', {'fields': (
            'description',
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

    def has_add_permission(self, request):
        return self.model.objects.count() < 1


@admin.register(PromoVisitor)
class PromoVisitorAdmin(admin.ModelAdmin):
    readonly_fields = ['get_post_display', 'user', 'ip']

    fields = ('form_data', 'get_post_display', 'user', 'ip')

    class Media:
        js = ('js/admin/promo.form.viewer.js',)
        css = {
            'all': ('js/admin/promo.form.viewer.css',)
        }

    def has_add_permission(self, request):
        return False


class PromoFormFieldInline(admin.StackedInline):
    model = PromoFormField
    extra = 1


@admin.register(PromoFormBuilder)
class PromoFormBuilderAdmin(admin.ModelAdmin):
    inlines = (PromoFormFieldInline,)

    exclude = ('captcha',)

    def has_add_permission(self, request):
        return self.model.objects.count() < 1
