from django.contrib import admin
from .models import *
from adminsortable2.admin import SortableAdminMixin

# Register your models here.


class CourseActionDateObjectInline(admin.StackedInline):
    model = CourseActionDateObject
    extra = 1

    readonly_fields = ['get_absolute_url']


@admin.register(CourseActionDateObject)
class CourseActionDateAdmin(admin.ModelAdmin):
    list_display = ['action_date', 'course', 'get_free_place_count', 'is_active', 'is_actual']
    list_filter = ['course', 'is_active', 'is_actual', 'action_date']
    search_fields = ['course']


@admin.register(Course)
class CourseAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['get_truncated_title', 'cost', 'schedule', 'get_already_applied_students_count', 'is_active', 'order_index']
    search_fields = ['title', 'slug', 'short_description', 'full_description']
    list_filter = ['is_active']

    inlines = (CourseActionDateObjectInline,)

    prepopulated_fields = {'slug': ('title',)}


@admin.register(ApplyRequest)
class ApplyRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'created_at', 'is_read', 'is_reacted', 'is_approved']
    list_filter = ['is_read', 'is_reacted', 'is_approved', 'created_at']

    readonly_fields = ['name', 'email', 'phone', 'education', 'message', 'course']
