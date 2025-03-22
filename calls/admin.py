from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse

from calls.models import Call


@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    readonly_fields = ['course_link', 'email', 'name', 'phone', 'message']
    list_display = ['__str__', 'course_link', 'email', 'created_at']
    list_filter = ['course']

    def course_link(self, instance):
        if not instance.course:
            return '-'

        return mark_safe('<a href="%(url)s">%(name)s</a>' % {
            'name': instance.course.title,
            'url': reverse('admin:schedule_course_change', kwargs={ 'object_id': instance.course.pk })
        })
