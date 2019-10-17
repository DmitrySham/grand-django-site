import json

from django.db import models

# Create your models here.


class Slider(models.Model):
    class Meta:
        verbose_name_plural = 'Слайдер на главной странице'
        verbose_name = 'Слайд'
        ordering = ('order_index',)

    order_index = models.PositiveIntegerField(default=0, verbose_name='Порядковый номер')
    is_active = models.BooleanField(default=True, verbose_name='Активно?')
    title = models.CharField(max_length=255, verbose_name='Название', null=True, blank=True)
    description = models.TextField(verbose_name='Описание', help_text='HTML теги разрешены', null=True, blank=True)
    link = models.CharField(
        max_length=1000,
        verbose_name='Сылка',
        null=True,
        blank=True,
        help_text='При нажатии на кнопку "Узнать больше" пользователь будет перенаправлен на эту ссылку.'
                  ' Если ссылку оставить пустым кнопка "Узнать больше" не будет отображаться'
    )

    thumbnail = models.FileField(
        upload_to='index-page-slider/',
        verbose_name='Изображение',
        help_text='Предпочтительный размер 1520x450'
    )

    def __str__(self):
        if self.title:
            return self.title
        return "Объект слайдера"


class SiteSettings(models.Model):
    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'

    footer_description = models.TextField(
        verbose_name='Описание в подвале',
        null=True, blank=True,
        help_text='Это описание выводится в подвале сайта под логотипом'
    )

    header_phone = models.CharField(
        max_length=255,
        verbose_name='Телефон',
        null=True, blank=True,
        help_text='Этот телефон выводится в верхней части сайта'
    )

    header_email = models.ForeignKey(
        to='AdminEmails',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name='Почта',
        help_text='Эта почта будет выводиться в верхней части сайта'
    )

    grand_smeta_text = models.TextField(verbose_name='Текст в Гранд Смета', null=True, blank=True)
    grand_smeta_header_image = models.FileField(verbose_name='Изображение на странице "Гранд Смета"', null=True, blank=True, upload_to='grand-smeta/headers/')
    news_header_image = models.FileField(verbose_name='Изображение на странице новостей', null=True, blank=True, upload_to='blog/headers/')
    schedule_header_image = models.FileField(verbose_name='Изображение на странице "Учебный центр"', null=True, blank=True, upload_to='schedule/headers/')
    one_c_header_image = models.FileField(verbose_name='Изображение на странице "1C"', null=True, blank=True, upload_to='1c/headers/')
    online_cash_box_header_image = models.FileField(verbose_name='Изображение на странице "Онлайн Кассы"', null=True, blank=True, upload_to='online-cahs-box/headers/')
    electronic_signature_header_image = models.FileField(verbose_name='Изображение на странице "Электронные подписи"', null=True, blank=True, upload_to='electronic-signature/headers/')

    # home page:
    index_page_text = models.TextField(verbose_name='Текст на главной странице', null=True, blank=True)
    why_choose_us = models.TextField(verbose_name='Почему выбирают нас?', null=True, blank=True)

    schedule = models.TextField(verbose_name='Текст учебного центра', null=True, blank=True)
    schedule_thumbnail = models.FileField(verbose_name='Изображение учебного центра', null=True, blank=True)
    schedule_list_items = models.TextField(verbose_name='Маркированный список учебного центра', default=json.dumps(list()), blank=True)

    grand_service = models.TextField(verbose_name='Текст Гранд Сервиса', null=True, blank=True)
    grand_service_thumbnail = models.FileField(verbose_name='Изображение гранд сервиса', null=True, blank=True)
    grand_service_list_items = models.TextField(verbose_name='Маркированный список гранд сервиса', default=json.dumps(list()), blank=True)

    grand_smeta = models.TextField(verbose_name='Текст Гранд Смета', null=True, blank=True)
    grand_smeta_thumbnail = models.FileField(verbose_name='Изображение Гранд смета', null=True, blank=True)
    grand_smeta_list_items = models.TextField(verbose_name='Маркированный список Гранд Смета', default=json.dumps(list()), blank=True)

    def __str__(self):
        return 'Настройки сайта'


class AdminEmails(models.Model):
    class Meta:
        verbose_name_plural = 'Почта администрации'
        verbose_name = 'Почта'

    is_active = models.BooleanField(default=True, verbose_name='Активный?')
    email = models.EmailField(verbose_name='Почта')

    def __str__(self):
        return self.email


class SocialProfileLinks(models.Model):
    class Meta:
        verbose_name = 'Ссылка на соц. сеть'
        verbose_name_plural = 'Ссылки на соц. сети'

    is_active = models.BooleanField(default=True, verbose_name='Активно?')
    title = models.CharField(max_length=255, verbose_name='Наименование', null=True, blank=True)
    url = models.URLField(verbose_name='Ссылка')
    icon = models.CharField(
        max_length=255,
        verbose_name='Иконка',
        help_text='Указываем класс для иконок. Например, "fa fa-facebook".'
                  ' Список иконок можно посмотреть <a href="https://fontawesome.com/v4.7.0/icons/" target="_blank">тут</a>'
    )
    settings = models.ForeignKey(to='SiteSettings', on_delete=models.CASCADE, verbose_name='Настройки')

    def __str__(self):
        if self.title:
            return self.title
        return str(self.url)


class FooterMenuLinks(models.Model):
    class Meta:
        verbose_name_plural = 'Ссылки в подвале сайта'
        verbose_name = 'Ссылка'

    is_active = models.BooleanField(default=True, verbose_name='Активно?')
    title = models.CharField(max_length=255, verbose_name='Отображаемый текст')
    on_blank = models.BooleanField(default=False, verbose_name='Открывать в новой странице?')
    link = models.CharField(max_length=255, verbose_name='Ссылка')
    settings = models.ForeignKey(to='SiteSettings', on_delete=models.CASCADE, verbose_name='Настройки')

    def __str__(self):
        return self.title


class GrandSmeta(models.Model):
    class Meta:
        verbose_name_plural = 'Гранд Смета'
        verbose_name = 'Гранд Смету'

    is_active = models.BooleanField(default=True, verbose_name='Активна?')
    thumbnail = models.FileField(upload_to='grand-smeta/', verbose_name='Изображение', help_text='Предпочтительные размеры: 540x380')
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.CharField(max_length=255, verbose_name='SLUG', unique=True, help_text='URL Endpoint name')
    short_description = models.TextField(verbose_name='Короткое описание', null=True, blank=False)
    description = models.TextField(verbose_name='Полное описание')
    price = models.CharField(verbose_name='Цена', max_length=255)

    def __str__(self):
        return self.title


class Contacts(models.Model):
    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    thumbnail = models.FileField(upload_to='contacts/header/', verbose_name='Изображение на странице контактов', null=True, blank=True)
    phones = models.TextField(default=json.dumps(list()), verbose_name='Телефоны', blank=True)
    emails = models.ManyToManyField(to='AdminEmails', blank=True, verbose_name='E-Mail\'ы')
    address = models.TextField(verbose_name='Адрес', null=True, blank=True)
    work_schedule = models.TextField(verbose_name='Режим работы', null=True, blank=True)

    def __str__(self):
        return 'Настройки контактов'


class Feedback(models.Model):
    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    is_read = models.BooleanField(default=False, verbose_name='Прочитано?')
    is_reacted = models.BooleanField(default=False, verbose_name='Отреагировали?')

    name = models.CharField(max_length=255, verbose_name='Имя')
    first_name = models.CharField(max_length=255, verbose_name='Имя', null=True, blank=True)
    last_name = models.CharField(max_length=255, verbose_name='Фамилия', null=True, blank=True)
    middle_name = models.CharField(max_length=255, verbose_name='Отчество', null=True, blank=True)
    email = models.EmailField(verbose_name='Почта')
    subject = models.CharField(max_length=255, verbose_name='Тема')
    message = models.TextField(verbose_name='Сообщение', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name
