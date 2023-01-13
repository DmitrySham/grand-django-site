from ckeditor_uploader.fields import RichTextUploadingField

from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.template.defaultfilters import truncatechars

from core.utils import SetUniqueName


# # Create your models here.


class Course(models.Model):
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ('order_index',)

    order_index = models.PositiveIntegerField(default=0, verbose_name='Порядок')
    is_active = models.BooleanField(default=True, verbose_name='Активно?')

    thumbnail = models.FileField(upload_to='schedule-objects/', verbose_name='Изображение', help_text='Предпочитаемые размеры: 540x380')
    atr_alt = models.CharField(max_length=255, verbose_name='Атрибут alt', null=True, blank=True)
    #cover_image = models.FileField(upload_to='schedule-objects/cover-images/', verbose_name='Обложка', null=True, blank=True)

    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.CharField(max_length=255, verbose_name='SLUG', unique=True, help_text='URL endpoint name')
    short_description = models.TextField(verbose_name='Краткое описание', null=True, blank=True)
    full_description = models.TextField(verbose_name='Полное описание')

    cost = models.CharField(max_length=255, verbose_name='Стоимость курса', null=True)
    # schedule = models.CharField(max_length=255, verbose_name='Расписание занятий', help_text='Это расписание будет отображаться на странице расписани', null=True)

    share_links = models.ManyToManyField(to='production.ShareLinks', blank=True, verbose_name='Ссылки поделиться')

    # Seo
    page_title = models.TextField(verbose_name='Тег title', null=True, blank=True)
    page_meta_keywords = models.TextField(verbose_name='Тег meta keywords', null=True, blank=True)
    page_meta_description = models.TextField(verbose_name='Тег meta description', null=True, blank=True)
    page_meta_og_title = models.TextField(verbose_name='Тег meta og:title', null=True, blank=True)
    page_meta_og_description = models.TextField(verbose_name='Тег meta og:description', null=True, blank=True)
    page_meta_og_image = models.TextField(verbose_name='Тег meta og:image', null=True, blank=True)

    # def get_actual_date_action(self):
    #     return self.courseactiondateobject_set.filter(is_active=True, is_actual=True).first()

    def __str__(self):
        return truncatechars(self.title, 40)

    def get_truncated_title(self):
        return self.__str__()

    get_truncated_title.short_description = 'Название'

    # def get_already_applied_students_count(self):
    #     action_object = self.courseactiondateobject_set.filter(is_active=True, is_actual=True).first()
    #
    #     if action_object:
    #         return action_object.applyrequest_set.count()
    #
    #     return 0

    # get_already_applied_students_count.short_description = 'Кол-во зап-ся на этот курс'


class Schedule(models.Model):
    class Meta:
        verbose_name_plural = 'Расписание'
        verbose_name = 'Расписание'

    start_date = models.TextField(verbose_name='Дата начала занятий')

    start_hour = models.TimeField(verbose_name='Время начала занятий')
    finish_hour = models.TimeField(verbose_name='Время конца занятий')
    days = models.TextField(verbose_name='Дни недель')

    duration = models.TextField(verbose_name='Продолжительность')

    have_own_cost = models.BooleanField(default=False, verbose_name='Другая цена?')
    cost = models.CharField(max_length=255, verbose_name='Цена', null=True, blank=True)

    course = models.ForeignKey(to=Course, on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return self.start_date


class License(models.Model):
    class Meta:
        verbose_name = 'Лицензия'
        verbose_name_plural = 'Лицензии'
        ordering = ('order_index',)

    order_index = models.PositiveIntegerField(default=0, verbose_name='Порядковый номер')
    title = models.CharField(max_length=255, verbose_name='Название', default='')
    image = models.ImageField(upload_to=SetUniqueName(), verbose_name='Изображение')
    is_active = models.BooleanField(default=True, verbose_name='Активно?')

    def __str__(self):
        return str(self.image)


class Educators(models.Model):
    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
        ordering = ('order_index',)

    is_active = models.BooleanField(default=True, verbose_name='Активно?')
    order_index = models.PositiveIntegerField(default=0, verbose_name='Порядковый номер')
    name = models.TextField(verbose_name='ФИО')
    slug = models.CharField(max_length=255, verbose_name='SLUG', null=True)
    photo = models.ImageField(upload_to=SetUniqueName('educators'), verbose_name='Фотография',
                              help_text='Желаемый размер изображения: 348x348')
    photo_alt = models.CharField(max_length=255, verbose_name='Значение атрибута alt', null=True, blank=True)
    short_description = models.TextField(verbose_name='Краткое описание', null=True, blank=True)
    full_description = RichTextUploadingField(verbose_name='Полное описание', null=True, blank=True)

    page_title = models.TextField(verbose_name='Значение <title>', null=True, blank=True)
    page_meta_keywords = models.TextField(verbose_name='META Keywords', null=True, blank=True)
    page_meta_description = models.TextField(verbose_name='META Description', null=True, blank=True)
    page_meta_og_title = models.TextField(verbose_name='META og:title', null=True, blank=True)
    page_meta_og_description = models.TextField(verbose_name='META og:description', null=True, blank=True)
    page_meta_og_image = models.TextField(verbose_name='META og:image', null=True, blank=True)

    def __str__(self):
        return self.name
