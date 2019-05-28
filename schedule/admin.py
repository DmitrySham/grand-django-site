from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist

from .models import *
from adminsortable2.admin import SortableAdminMixin

# Register your models here.


class CourseActionDateObjectInline(admin.StackedInline):
    model = CourseActionDateObject
    extra = 0

    readonly_fields = ['get_absolute_url']


class ApplyRequestInline(admin.StackedInline):
    model = ApplyRequest

    fields = ['is_approved', 'name', 'email', 'phone', 'education', 'message', 'get_course_link']
    readonly_fields = fields

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(CourseActionDateObject)
class CourseActionDateAdmin(admin.ModelAdmin):
    list_display = ['action_date', 'course', 'get_free_place_count', 'is_active', 'is_actual']
    list_filter = ['course', 'is_active', 'is_actual', 'action_date']
    search_fields = ['course']

    inlines = (ApplyRequestInline,)


@admin.register(Course)
class CourseAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['get_truncated_title', 'cost', 'schedule', 'get_already_applied_students_count', 'is_active', 'order_index']
    search_fields = ['title', 'slug', 'short_description', 'full_description']
    list_filter = ['is_active']

    inlines = (CourseActionDateObjectInline,)

    prepopulated_fields = {'slug': ('title',)}


@admin.register(ApplyRequest)
class ApplyRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_course_title', 'created_at', 'is_read', 'is_reacted', 'is_approved']
    list_filter = ['is_read', 'is_reacted', 'is_approved', 'created_at']

    readonly_fields = ['name', 'email', 'phone', 'education', 'message', 'get_course_date_action_link', 'is_read']

    def get_course_title(self, obj):
        return obj.course.course.get_truncated_title()

    get_course_title.short_description = 'Курс'
    get_course_title.allow_tags = True

    def change_view(self, request, object_id, form_url='', extra_context=None):
        try:
            apply_request = ApplyRequest.objects.get(id=object_id)
            if not apply_request.is_read:
                apply_request.is_read = True
                apply_request.save()
        except ObjectDoesNotExist:
            pass
        return super(ApplyRequestAdmin, self).change_view(request, object_id, form_url=form_url, extra_context=extra_context)
