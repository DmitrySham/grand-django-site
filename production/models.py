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

    def __str__(self):
        return self.title
