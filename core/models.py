from django.db import models

# Create your models here.


class Slider(models.Model):
    class Meta:
        verbose_name_plural = 'Слайдер на главной странице'
        verbose_name = 'Слайд'

    is_active = models.BooleanField(default=True, verbose_name='Активно?')
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', help_text='HTML теги разрешены')
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
        return self.title


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
