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

    video_iframe = models.TextField(null=True, blank=True)
    course_roadmap_description = models.CharField(max_length=255, verbose_name='Описание под "Программа кураса"', null=True, blank=True)
    advantages = models.ManyToManyField(to='CourseAdvantages', blank=True)

    show_banner = models.BooleanField(default=True)
    logo = models.FileField(upload_to=SetUniqueName('courses/logos'), null=True, blank=True)
    banner_background = models.FileField(upload_to=SetUniqueName('courses/banners'), null=True, blank=True)

    course_roadmap_content = RichTextUploadingField(null=True, blank=True)
    subscription_plans = models.ManyToManyField(to='SubscriptionPlans', blank=True)

    siblings = models.ManyToManyField(to='Course', blank=True)

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


class CourseAdvantages(models.Model):
    class Meta:
        verbose_name = 'Приемущества курса'
        verbose_name_plural = 'Приемущества курса'

    is_active = models.BooleanField(default=True)
    icon = models.CharField(max_length=255, verbose_name='Название CSS класса для иконки')
    text = models.TextField()

    def __str__(self):
        return self.text


class SubscriptionPlans(models.Model):
    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'
        ordering = ('sort_index',)

    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, verbose_name='CSS класс для иконки', help_text='Сюда вписывается название класса иконки из <a href="https://fontawesome.com/v4.7.0/icons/" target="_blank">Font Awesome</a>. Предосмотр: <i class="fa id_icon_preview" data-syntax="full"></i>')
    action_name = models.CharField(max_length=255, verbose_name='Текст на кнопке')
    sort_index = models.PositiveIntegerField(default=0, verbose_name='Номер для сортировки.')
    action = models.CharField(max_length=255, verbose_name='Действие на клик', choices=(
        ('redirect', 'Перенаправить на другую страницу'),
        ('feedback', 'Показать форму обратной связи'),
    ), default='anchor')
    payment_url = models.URLField(null=True, blank=True)

    def has_mentor(self):
        return self.icon == 'fa fa-group'

    def __str__(self):
        return self.name


class SubscriptionPlanCharacteristicsDict(models.Model):
    class Meta:
        verbose_name = 'Словарь характеристик тарифов'
        verbose_name_plural = 'Словарь характеристик тарифов'

    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name


class SubscriptionPlanCharacteristics(models.Model):
    class Meta:
        verbose_name = 'Характеристика тарифа'
        verbose_name_plural = 'Характеристики тарифов'
        ordering = ('order_index',)

    is_active = models.BooleanField(default=True)
    name = models.ForeignKey(to='SubscriptionPlanCharacteristicsDict', on_delete=models.CASCADE, null=True)
    enabled = models.BooleanField(default=True)
    plan = models.ForeignKey(to='SubscriptionPlans', related_name='characteristic', on_delete=models.CASCADE)
    order_index = models.PositiveIntegerField(default=0)

    def __str__(self):
        if not self.name:
            return str(self.id)
        return self.name.name

