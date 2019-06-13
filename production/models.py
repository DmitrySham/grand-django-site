import json

from django.db import models

# Create your models here.


class OneC(models.Model):
    class Meta:
        verbose_name = '1С'
        verbose_name_plural = '1С'

    is_active = models.BooleanField(default=True, verbose_name='Активно?')
    title = models.CharField(max_length=255, verbose_name='Название 1С услуги')
    short_description = models.TextField(verbose_name='Краткое описание')
    full_description = models.TextField(verbose_name='Полное описание')
    thumbnail = models.FileField(
        upload_to='production/one-c/',
        verbose_name='Изображение',
        help_text='Предпочитаемые размеры 540x540'
    )
    cover_image = models.FileField(
        upload_to='production/one-c/cover-images/',
        verbose_name='Обложка',
        null=True,
        blank=True
    )
    price = models.CharField(max_length=255, verbose_name='Цена')

    def __str__(self):
        return self.title


class OnlineCashbox(models.Model):
    class Meta:
        verbose_name_plural = 'Онлайн кассы'
        verbose_name = 'Онлайн касса'

    is_active = models.BooleanField(default=True, verbose_name='Активный')
    title = models.CharField(max_length=255, verbose_name='Название')
    short_description = models.TextField(verbose_name='Короткое описание', null=True, blank=True)
    full_description = models.TextField(verbose_name='Полное описание', null=True, blank=True)

    price_box = models.TextField(verbose_name='Расценка', default=json.dumps(list()))

    thumbnail = models.FileField(
        upload_to='production/online-cashbox/',
        verbose_name='Изображение',
        help_text='Предпочитаемые размеры 540x540'
    )
    cover_image = models.FileField(
        upload_to='production/online-cashbox/cover-images/',
        verbose_name='Обложка',
        null=True, blank=True
    )

    share_links = models.ManyToManyField(to='ShareLinks', blank=True, verbose_name='Share ссылки')

    def __str__(self):
        return self.title


class OnlineCashBoxPartner(models.Model):
    class Meta:
        verbose_name_plural = 'Слайдер на странице Онлайн кассы'
        verbose_name = 'Слайдер на странице Онлайн кассы'

    is_active = models.BooleanField(default=True, verbose_name='Активно?')
    title = models.CharField(max_length=255, verbose_name='Название')
    thumbnail = models.FileField(upload_to='online-cash-box/thumbnails/', verbose_name='Изображение')

    def __str__(self):
        return self.title


class ShareLinks(models.Model):
    class Meta:
        verbose_name = 'Поделиться'
        verbose_name_plural = 'Ссылки поделится'

    is_active = models.BooleanField(default=True, verbose_name='Активный?')
    title = models.CharField(max_length=255, verbose_name='Название')
    url = models.TextField(
        max_length=1000,
        verbose_name='Ссылка',
        help_text='Ссылка которая ведет для того, что бы поделиться ссылкой. Параметр <b>{url}</b> нужен для ссылки на стриницу, <b>{title}</b> - для названия, <b>{description}</b> - Описание и <b>{image}</b> для изображения'
    )
    icon = models.CharField(
        max_length=50,
        verbose_name='Иконка',
        help_text='Сюда вписывается название класса иконки из <a href="https://fontawesome.com/v4.7.0/icons/" target="_blank">Font Awesome</a>. Предосмотр: <i class="fa id_icon_preview"></i>'
    )

    def __str__(self):
        return self.title


class ElectronicSignature(models.Model):
    class Meta:
        verbose_name_plural = 'Электронные подписи'
        verbose_name = 'Эл. подпись'

    is_active = models.BooleanField(default=True, verbose_name='Активный?')
    thumbnail = models.FileField(upload_to='production/electronic-signature/', verbose_name='Изображение', null=True)
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.CharField(max_length=255, verbose_name='SLUG', unique=True)
    short_description = models.TextField(verbose_name='Краткое описание', null=True, blank=True)
    full_description = models.TextField(verbose_name='Полное описание')
    price_box = models.TextField(verbose_name='Цены', default=json.dumps(list()))

    share_links = models.ManyToManyField(to='ShareLinks', blank=True, verbose_name='Share ссылки')

    def __str__(self):
        return self.title
