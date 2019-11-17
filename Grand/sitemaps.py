from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import Post
from core.models import GrandSmeta
from production.models import OneC, OnlineCashbox
from schedule.models import Course


class PostSitemap(Sitemap):

    def items(self):
        return Post.objects.all().order_by('-created_at')

    def location(self, obj):
        return reverse('blog:single', kwargs={'slug': obj.slug})

    def lastmod(self, obj):
        return obj.created_at


class GrandSmetaSitemap(Sitemap):

    def items(self):
        return GrandSmeta.objects.all()

    def location(self, obj):
        return reverse('core:grand_smeta_single', kwargs={'slug': obj.slug})


class OneCSitemap(Sitemap):

    def items(self):
        return OneC.objects.all()

    def location(self, obj):
        return reverse('production:one_c_single', kwargs={'id': obj.id})


class OnlineCashboxSitemap(Sitemap):

    def items(self):
        return OnlineCashbox.objects.all()

    def location(self, obj):
        return reverse('production:online_cashbox_single', kwargs={'id': obj.id})


class CourseSitemap(Sitemap):

    def items(self):
        return Course.objects.all()

    def location(self, obj):
        return reverse('schedule:single', kwargs={'slug': obj.slug})


class StaticPagesSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return [
            'index',
            'production:one_c_list',
            'production:online_cashbox_list',
            'core:grand_smeta_list',
            'core:contacts',
            'schedule:list',
            'schedule:base_view',
            'blog:list'
        ]

    def location(self, obj):
        return reverse(obj)
