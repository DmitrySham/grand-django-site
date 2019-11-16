from .models import SiteSettings, Seo
from Grand.settings import SITE_VERSION
from blog.models import Post


def generate_view_params(request):
    return {
        'site_settings': SiteSettings.objects.first(),
        'site_version': SITE_VERSION,
        'last_posts': Post.objects.filter(is_active=True).order_by('-created_at')[:3],
        'seo': Seo.objects.first()
    }
