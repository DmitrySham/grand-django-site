from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.template.defaultfilters import truncatechars


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


#
#
# class CourseActionDateObject(models.Model):
#     class Meta:
#         verbose_name_plural = 'Информация о курсе'
#         verbose_name = 'Информация'
#
#     course = models.ForeignKey(to='Course', on_delete=models.CASCADE, verbose_name='Курс')
#     is_active = models.BooleanField(default=True, verbose_name='Активна?', help_text='Уберите этот флажок и эта дата станет не активная. Сайт будет брать дату начала обучения и кол-во свободных мест из <b>первого актуального</b> объекта даты среди всех <b>активных</b>')
#     is_actual = models.BooleanField(default=True, verbose_name='Актуально?', help_text='Уберите этот флажок и записи на эту дату прекратятся')
#     action_date = models.DateTimeField(verbose_name='Дата начала курса')
#     duration = models.CharField(max_length=255, verbose_name='Продолжительность')
#     max_people_in_course = models.PositiveIntegerField(default=0, verbose_name='Максимальное количество мест на обучение')
#
#     def get_free_place_count(self):
#         return str(self.max_people_in_course - self.applyrequest_set.filter(is_approved=True).count())
#
#     get_free_place_count.short_description = 'Кол-во св-х мест'
#     get_free_place_count.help_text = '(Макс. кол-во св-х мест) - (Кол-во <b>Подтвержденных</b> запросов на запись) = (Кол-во св-х мест)'
#
#     def get_absolute_url(self):
#         if not self.id:
#             return mark_safe('<strong>Просмотр записей пока не доступно</strong>')
#
#         content_type = ContentType.objects.get_for_model(self.__class__)
#         return mark_safe('<a href="%s#/tab/inline_0/">Посмотреть записавшихся</a>' % reverse_lazy("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,)))
#
#     get_absolute_url.short_description = 'Записавшиеся'
#
#     def __str__(self):
#         return 'Дата начала обучения "%(title)s"' % {
#             'title': self.course.__str__()
#         }
#
#
# class ApplyRequest(models.Model):
#     class Meta:
#         verbose_name = 'Запрос'
#         verbose_name_plural = 'Запросы на запись'
#
#     is_read = models.BooleanField(default=False, verbose_name='Прочитано?')
#     is_reacted = models.BooleanField(default=False, verbose_name='Отреагировано?')
#     is_approved = models.BooleanField(default=False, verbose_name='Подтвержденно?')
#
#     # name = models.CharField(max_length=255, verbose_name='ФИО')
#     first_name = models.CharField(max_length=255, verbose_name='Имя', null=True, blank=True)
#     last_name = models.CharField(max_length=255, verbose_name='Фамилия', null=True, blank=True)
#     middle_name = models.CharField(max_length=255, verbose_name='Отчество', null=True, blank=True)
#     email = models.EmailField(verbose_name='Электронная почта')
#     education = models.ForeignKey(to='Educations', on_delete=models.SET_NULL, null=True, max_length=255, verbose_name='Оброзование')
#     message = models.TextField(verbose_name='Сообщение')
#     phone = models.CharField(verbose_name='Телефон', null=True, max_length=255)
#
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
#
#     course = models.ForeignKey(to=CourseActionDateObject, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Курс')
#
#     def __str__(self):
#         return self.first_name + ' ' + self.last_name
#
#     def get_course_date_action_link(self):
#         content_type = ContentType.objects.get_for_model(self.course.__class__)
#         return mark_safe('<a href="%(url)s">%(title)s</a>' % {
#             'url': reverse_lazy("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.course.id,)),
#             'title': self.course.course.get_truncated_title()
#         })
#
#     get_course_date_action_link.short_description = 'Курс'
#
#     def get_course_link(self):
#         content_type = ContentType.objects.get_for_model(self.course.course.__class__)
#         return mark_safe('<a href="%(url)s">%(title)s</a>' % {
#             'url': reverse_lazy("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.course.course.id,)),
#             'title': self.course.course.get_truncated_title()
#         })
#
#
# class Educations(models.Model):
#     class Meta:
#         verbose_name_plural = 'Образования(Словарь)'
#         verbose_name = 'Образование'
#
#     title = models.CharField(max_length=255, verbose_name='Название')
#
#     def __str__(self):
#         return self.title


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
