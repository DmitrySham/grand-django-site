"""Grand URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core import views as core_views
from django.conf.urls import handler404, handler500
from django.views.generic import TemplateView
from Grand import settings
from django.contrib.sitemaps.views import sitemap

from production.views import online_cashbox_list, one_c_single, one_c_list
from schedule.views import course_single
from .sitemaps import *

sitemaps = {
    'static': StaticPagesSitemap,
    'post': PostSitemap,
    'grand_smeta': GrandSmetaSitemap,
    'one_c': OneCSitemap,
    'online_cashbox': OnlineCashboxSitemap,
    'courses': CourseSitemap,
}

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('production/', include(('production.urls', 'production'))),
    path('core/', include(('core.urls', 'core'))),
    path('schedule/', include(('schedule.urls', 'schedule'))),
    path('news/', include(('blog.urls', 'blog'))),
    path('checkouts/', include(('checkouts.urls', 'checkouts'))),
    path('calls/', include(('calls.urls', 'calls'))),

    path('yandex_88e2184967f12b8a.html', TemplateView.as_view(template_name='yandex_88e2184967f12b8a.html')),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('manifest.xml', TemplateView.as_view(template_name='manifest.xml', content_type='text/xml')),
    path('sitemap.xml', TemplateView.as_view(template_name='sitemap.xml', content_type='text/xml')),
    #path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    # path('1c/predpriyatie/', include(('production.urls', 'production'))),
    path('1c/predpriyatie/', one_c_list, name='one_c_list'),
    path('1c/<str:slug>/', one_c_single, name='one_c_single'),
    path('courses/<str:slug>/', course_single, name='courses_single'),
    path('online-kassa/', online_cashbox_list, name='online_cashbox_list'),
    path('', core_views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = core_views.handler404
handler500 = core_views.handler500
