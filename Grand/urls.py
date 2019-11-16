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

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('production/', include(('production.urls', 'production'))),
    path('core/', include(('core.urls', 'core'))),
    path('schedule/', include(('schedule.urls', 'schedule'))),
    path('news/', include(('blog.urls', 'blog'))),

    path('yandex_88e2184967f12b8a.html', TemplateView.as_view(template_name='yandex_88e2184967f12b8a.html')),
    path('robot.txt', TemplateView.as_view(template_name='robot.txt', content_type='text/plain')),
    path('manifest.xml', TemplateView.as_view(template_name='manifest.xml', content_type='text/xml')),

    path('', core_views.index, name='index'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = core_views.handler404
handler500 = core_views.handler500

