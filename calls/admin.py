from django.contrib import admin

from calls.models import Call


@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    readonly_fields = ['course', 'name', 'phone', 'message']
    list_display = ['__str__', 'course', 'created_at']
