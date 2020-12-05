from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import truncatechars
# Create your models here.


class Post(models.Model):
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    is_active = models.BooleanField(default=True, verbose_name='Активна?')

    thumbnail = models.FileField(upload_to='blog/', null=True, blank=False, verbose_name='Изображение')
    atr_alt = models.CharField(max_length=255, verbose_name='Атрибут alt', null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.CharField(max_length=255, verbose_name='SLUG', unique=True)

    short_description = models.TextField(verbose_name='Краткое описание', null=True, blank=True)

    content = RichTextUploadingField(verbose_name='Тело статьи')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    is_promo = models.BooleanField(default=False, verbose_name='Включить заполнение данных')

    # Seo
    page_title = models.TextField(verbose_name='Тег title', null=True, blank=True)
    page_meta_keywords = models.TextField(verbose_name='Тег meta keywords', null=True, blank=True)
    page_meta_description = models.TextField(verbose_name='Тег meta description', null=True, blank=True)
    page_meta_og_title = models.TextField(verbose_name='Тег meta og:title', null=True, blank=True)
    page_meta_og_description = models.TextField(verbose_name='Тег meta og:description', null=True, blank=True)
    page_meta_og_image = models.TextField(verbose_name='Тег meta og:image', null=True, blank=True)

    def __str__(self):
        return truncatechars(self.title, 100)

    def get_truncated_title(self):
        return self.__str__()

    get_truncated_title.short_description = 'Название'
