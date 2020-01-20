from django.contrib import admin
from django.contrib.admin.utils import flatten_fieldsets

from .models import Checkout


@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

    def get_readonly_fields(self, request, obj=None):
        return [field.name for field in self.opts.local_fields]
