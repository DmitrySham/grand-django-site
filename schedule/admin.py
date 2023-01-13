from adminsortable2.admin import SortableAdminMixin

from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Course, License, Schedule, Educators


class ScheduleAdminInline(admin.StackedInline):
    model = Schedule
    extra = 1


@admin.register(Course)
class CourseAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['get_truncated_title', 'cost', 'is_active', 'order_index']
    search_fields = ['title', 'slug', 'short_description', 'full_description']
    list_filter = ['is_active']

    inlines = (ScheduleAdminInline,)

    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        ('Общее', {'fields': (
            'is_active',
            'thumbnail',
            'atr_alt',
            #'cover_image',
            'title',
            'slug',
            'short_description',
            'full_description',
            'cost',
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


@admin.register(License)
class LicenseAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'image', 'order_index']

    class Media:
        css = {
            'all': (
                'js/admin/image.field.css',
            )
        }
        js = (
            'js/admin/image.field.js',
        )


@admin.register(Educators)
class EducatorsAdmin(SortableAdminMixin, admin.ModelAdmin):
    class Media:
        css = {'all': (
            'js/admin/image.field.css',
        )}
        js = (
            'js/admin/image.field.js',
        )

    list_display = ['order_index', 'name', 'photo_representation', 'short_description', 'is_active']
    prepopulated_fields = {'slug': ('name',)}

    fieldsets = (
        (None, {'fields': (
            'is_active',
            'name',
            'slug',
        )}),
        ('Фотография', {'fields': (
            'photo',
            'photo_alt',
        )}),
        ('Описание', {'fields': (
            'short_description',
            'full_description',
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

    def photo_representation(self, instance):
        html = '<img src="%(url)s" alt="%(name)s" style="max-width: 100px" />' % {
            'url': instance.photo.url,
            'name': instance.name
        }
        return mark_safe(html)
    photo_representation.short_description = 'Фотография'
