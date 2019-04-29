from .models import SiteSettings
from Grand.settings import SITE_VERSION


def generate_view_params(request):
    return {
        'site_settings': SiteSettings.objects.first(),
        'site_version': SITE_VERSION
    }
