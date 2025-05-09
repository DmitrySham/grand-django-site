import json

from ckeditor_uploader.fields import RichTextUploadingField
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
    one_c_text = RichTextUploadingField(verbose_name='Текст в 1С', null=True, blank=True)
    one_c_h1_text = models.CharField(verbose_name='<h1> тег на странице  "1C"', max_length=255, null=True, blank=True)
    one_c_header_image = models.FileField(verbose_name='Изображение на странице "1C"', null=True, blank=True, upload_to='1c/headers/')
    online_cash_box_text = models.TextField(verbose_name='Текст в Онлайн-кассах', null=True, blank=True)
    online_cash_box_h1_text = models.CharField(verbose_name='<h1> тег на странице "Онлайн Кассы"', max_length=255, null=True, blank=True)
    online_cash_box_header_image = models.FileField(verbose_name='Изображение на странице "Онлайн Кассы"', null=True, blank=True, upload_to='online-cahs-box/headers/')
    electronic_signature_header_image = models.FileField(verbose_name='Изображение на странице "Электронные подписи"', null=True, blank=True, upload_to='electronic-signature/headers/')

    # home page:
    index_page_text = RichTextUploadingField(verbose_name='Текст на главной странице', null=True, blank=True)
    index_page_h1_text = models.CharField(verbose_name='<h1> тег на главной странице', max_length=255, null=True, blank=True)
    why_choose_us = RichTextUploadingField(verbose_name='Текст на главной странице', null=True, blank=True)

    schedule = models.TextField(verbose_name='Текст учебного центра', null=True, blank=True)
    schedule_thumbnail = models.FileField(verbose_name='Изображение учебного центра', null=True, blank=True)
    schedule_list_items = models.TextField(verbose_name='Маркированный список учебного центра', default=json.dumps(list()), blank=True)

    grand_service = models.TextField(verbose_name='Текст Гранд Сервиса', null=True, blank=True)
    grand_service_thumbnail = models.FileField(verbose_name='Изображение гранд сервиса', null=True, blank=True)
    grand_service_list_items = models.TextField(verbose_name='Маркированный список гранд сервиса', default=json.dumps(list()), blank=True)

    grand_smeta = models.TextField(verbose_name='Текст Гранд Смета', null=True, blank=True)
    grand_smeta_thumbnail = models.FileField(verbose_name='Изображение Гранд смета', null=True, blank=True)
    grand_smeta_list_items = models.TextField(verbose_name='Маркированный список Гранд Смета', default=json.dumps(list()), blank=True)

    icon_heading = models.CharField(max_length=255, verbose_name='Название раздела с иконками', null=True, blank=True)
    icon_1c = models.TextField(verbose_name='Текст для иконки 1С', null=True, blank=True)
    icon_online_cashbox = models.TextField(verbose_name='Текст для иконки Онлайн Касс', null=True, blank=True)
    icon_schedule = models.TextField(verbose_name='Текст для иконки Учебного центра', null=True, blank=True)
    icon_grand_smeta = models.TextField(verbose_name='Текст для иконки Гранд Смета', null=True, blank=True)
    icon_electronic_sign = models.TextField(verbose_name='Текст для иконки Электронные подписи', null=True, blank=True)
    icon_certificates = models.TextField(verbose_name='текст для иконки Сертификаты', null=True, blank=True)

    educators_h1_text = models.CharField(verbose_name='<h1> тег на странице "Преподаватели"', max_length=255, null=True, blank=True)
    educators_text = RichTextUploadingField(verbose_name='Текст на странице "Преподаватели"', null=True, blank=True)

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
    art_alt = models.CharField(max_length=255, verbose_name='Атрибут alt', null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.CharField(max_length=255, verbose_name='SLUG', unique=True, help_text='URL Endpoint name')
    short_description = models.TextField(verbose_name='Короткое описание', null=True, blank=False)
    description = models.TextField(verbose_name='Полное описание')
    price = models.CharField(verbose_name='Цена', max_length=255)

    # Seo
    page_title = models.TextField(verbose_name='Тег title', null=True, blank=True)
    page_meta_keywords = models.TextField(verbose_name='Тег meta keywords', null=True, blank=True)
    page_meta_description = models.TextField(verbose_name='Тег meta description', null=True, blank=True)
    page_meta_og_title = models.TextField(verbose_name='Тег meta og:title', null=True, blank=True)
    page_meta_og_description = models.TextField(verbose_name='Тег meta og:description', null=True, blank=True)
    page_meta_og_image = models.TextField(verbose_name='Тег meta og:image', null=True, blank=True)

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
    email = models.EmailField(verbose_name='Почта', null=True, blank=True, default='')
    phone = models.CharField(max_length=255, verbose_name='Телефон', null=True)
    subject = models.CharField(max_length=255, verbose_name='Тема')
    message = models.TextField(verbose_name='Сообщение', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name


class Seo(models.Model):
    class Meta:
        verbose_name_plural = 'SEO'
        verbose_name = 'SEO'

    # index page
    index_page_title = models.TextField(verbose_name='Тег title', null=True, blank=True)
    index_page_meta_keywords = models.TextField(verbose_name='Тег meta keywords', null=True, blank=True)
    index_page_meta_description = models.TextField(verbose_name='Тег meta description', null=True, blank=True)
    index_page_meta_og_title = models.TextField(verbose_name='Тег meta og:title', null=True, blank=True)
    index_page_meta_og_description = models.TextField(verbose_name='Тег meta og:description', null=True, blank=True)
    index_page_meta_og_image = models.TextField(verbose_name='Тег meta og:image', null=True, blank=True)

    # blog list
    blog_list_page_title = models.TextField(verbose_name='Тег title', null=True, blank=True)
    blog_list_page_meta_keywords = models.TextField(verbose_name='Тег meta keywords', null=True, blank=True)
    blog_list_page_meta_description = models.TextField(verbose_name='Тег meta description', null=True, blank=True)
    blog_list_page_meta_og_title = models.TextField(verbose_name='Тег meta og:title', null=True, blank=True)
    blog_list_page_meta_og_description = models.TextField(verbose_name='Тег meta og:description', null=True, blank=True)
    blog_list_page_meta_og_image = models.TextField(verbose_name='Тег meta og:image', null=True, blank=True)

    # grand smeta list
    grand_smeta_list_page_title = models.TextField(verbose_name='Тег title', null=True, blank=True)
    grand_smeta_list_page_meta_keywords = models.TextField(verbose_name='Тег meta keywords', null=True, blank=True)
    grand_smeta_list_page_meta_description = models.TextField(verbose_name='Тег meta description', null=True, blank=True)
    grand_smeta_list_page_meta_og_title = models.TextField(verbose_name='Тег meta og:title', null=True, blank=True)
    grand_smeta_list_page_meta_og_description = models.TextField(verbose_name='Тег meta og:description', null=True, blank=True)
    grand_smeta_list_page_meta_og_image = models.TextField(verbose_name='Тег meta og:image', null=True, blank=True)

    # one c
    one_c_list_page_title = models.TextField(verbose_name='Тег title', null=True, blank=True)
    one_c_list_page_meta_keywords = models.TextField(verbose_name='Тег meta keywords', null=True, blank=True)
    one_c_list_page_meta_description = models.TextField(verbose_name='Тег meta description', null=True, blank=True)
    one_c_list_page_meta_og_title = models.TextField(verbose_name='Тег meta og:title', null=True, blank=True)
    one_c_list_page_meta_og_description = models.TextField(verbose_name='Тег meta og:description', null=True, blank=True)
    one_c_list_page_meta_og_image = models.TextField(verbose_name='Тег meta og:image', null=True, blank=True)

    # online cashbox
    online_cashbox_list_page_title = models.TextField(verbose_name='Тег title', null=True, blank=True)
    online_cashbox_list_page_meta_keywords = models.TextField(verbose_name='Тег meta keywords', null=True, blank=True)
    online_cashbox_list_page_meta_description = models.TextField(verbose_name='Тег meta description', null=True, blank=True)
    online_cashbox_list_page_meta_og_title = models.TextField(verbose_name='Тег meta og:title', null=True, blank=True)
    online_cashbox_list_page_meta_og_description = models.TextField(verbose_name='Тег meta og:description', null=True, blank=True)
    online_cashbox_list_page_meta_og_image = models.TextField(verbose_name='Тег meta og:image', null=True, blank=True)

    # schedule table
    schedule_table_page_title = models.TextField(verbose_name='Тег title', null=True, blank=True)
    schedule_table_page_meta_keywords = models.TextField(verbose_name='Тег meta keywords', null=True, blank=True)
    schedule_table_page_meta_description = models.TextField(verbose_name='Тег meta description', null=True, blank=True)
    schedule_table_page_meta_og_title = models.TextField(verbose_name='Тег meta og:title', null=True, blank=True)
    schedule_table_page_meta_og_description = models.TextField(verbose_name='Тег meta og:description', null=True, blank=True)
    schedule_table_page_meta_og_image = models.TextField(verbose_name='Тег meta og:image', null=True, blank=True)

    # schedule list
    schedule_list_page_title = models.TextField(verbose_name='Тег title', null=True, blank=True)
    schedule_list_page_meta_keywords = models.TextField(verbose_name='Тег meta keywords', null=True, blank=True)
    schedule_list_page_meta_description = models.TextField(verbose_name='Тег meta description', null=True, blank=True)
    schedule_list_page_meta_og_title = models.TextField(verbose_name='Тег meta og:title', null=True, blank=True)
    schedule_list_page_meta_og_description = models.TextField(verbose_name='Тег meta og:description', null=True, blank=True)
    schedule_list_page_meta_og_image = models.TextField(verbose_name='Тег meta og:image', null=True, blank=True)

    # contacts
    contacts_page_title = models.TextField(verbose_name='Тег title', null=True, blank=True)
    contacts_page_meta_keywords = models.TextField(verbose_name='Тег meta keywords', null=True, blank=True)
    contacts_page_meta_description = models.TextField(verbose_name='Тег meta description', null=True, blank=True)
    contacts_page_meta_og_title = models.TextField(verbose_name='Тег meta og:title', null=True, blank=True)
    contacts_page_meta_og_description = models.TextField(verbose_name='Тег meta og:description', null=True, blank=True)
    contacts_page_meta_og_image = models.TextField(verbose_name='Тег meta og:image', null=True, blank=True)

    # licenses
    licenses_page_title = models.TextField(verbose_name='Тег title', null=True, blank=True)
    licenses_page_meta_keywords = models.TextField(verbose_name='Тег meta keywords', null=True, blank=True)
    licenses_page_meta_description = models.TextField(verbose_name='Тег meta description', null=True, blank=True)
    licenses_page_meta_og_title = models.TextField(verbose_name='Тег meta og:title', null=True, blank=True)
    licenses_page_meta_og_description = models.TextField(verbose_name='Тег meta og:description', null=True, blank=True)
    licenses_page_meta_og_image = models.TextField(verbose_name='Тег meta og:image', null=True, blank=True)

    # Educators
    educators_page_title = models.TextField(verbose_name='Тег title', null=True, blank=True)
    educators_page_meta_keywords = models.TextField(verbose_name='Тег meta keywords', null=True, blank=True)
    educators_page_meta_description = models.TextField(verbose_name='Тег meta description', null=True, blank=True)
    educators_page_meta_og_title = models.TextField(verbose_name='Тег meta og:title', null=True, blank=True)
    educators_page_meta_og_description = models.TextField(verbose_name='Тег meta og:description', null=True, blank=True)
    educators_page_meta_og_image = models.TextField(verbose_name='Тег meta og:image', null=True, blank=True)

    def __str__(self):
        return 'Настройки META тегов'


class PrivacyPolicy(models.Model):
    class Meta:
        verbose_name = 'Политика конфиденциальности'
        verbose_name_plural = 'Политика конфиденциальности'

    description = RichTextUploadingField(verbose_name='Описание', null=True, blank=True)

    # Seo
    page_title = models.TextField(verbose_name='Тег title', null=True, blank=True)
    page_meta_keywords = models.TextField(verbose_name='Тег meta keywords', null=True, blank=True)
    page_meta_description = models.TextField(verbose_name='Тег meta description', null=True, blank=True)
    page_meta_og_title = models.TextField(verbose_name='Тег meta og:title', null=True, blank=True)
    page_meta_og_description = models.TextField(verbose_name='Тег meta og:description', null=True, blank=True)
    page_meta_og_image = models.TextField(verbose_name='Тег meta og:image', null=True, blank=True)

    def __str__(self):
        return 'Политика конфиденциальности'


class PromoVisitor(models.Model):
    class Meta:
        verbose_name = 'Заполненные данные с новостей'
        verbose_name_plural = 'Заполненные данные с новостей'

    post = models.ForeignKey(
        to='blog.Post',
        on_delete=models.CASCADE,
        verbose_name='Пост',
    )
    user = models.ForeignKey(
        to='account.Account',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name='Пользователь'
    )
    ip = models.CharField(max_length=15, verbose_name='IP пользователя')
    form_data = models.TextField(verbose_name='Данные формы', default='{}')

    def __str__(self):
        return self.ip

    def get_post_display(self):
        return json.dumps({
            'id': self.post.id,
            'title': self.post.title,
            'slug': self.post.slug
        })

    get_post_display.short_description = 'Пост'


class PromoFormBuilder(models.Model):
    class Meta:
        verbose_name_plural = 'Форма отображаемая в новостях'
        verbose_name = 'Форма'

    privacy_policy = models.BooleanField(default=True, verbose_name='Отображать "Политика конфеденциальности"?')
    captcha = models.BooleanField(default=True, verbose_name='Использовать Google-Captcha?')

    def __str__(self):
        return 'Форма'


class PromoFormField(models.Model):
    class Meta:
        verbose_name_plural = 'Поля для формы'
        verbose_name = 'Поле'

    form = models.ForeignKey(to='PromoFormBuilder', on_delete=models.CASCADE, verbose_name='Форма')
    field_type = models.CharField(
        max_length=255,
        verbose_name='Тип поля',
        choices=(
            ('text', 'Текст'),
            ('email', 'Email'),
            ('tel', 'Телефон'),
            ('textarea', 'Большое поле для текста'),
        )
    )
    field_placeholder = models.CharField(max_length=100, verbose_name='Название поля (макс. 100 символов)')
    required = models.BooleanField(default=False, verbose_name='Обязательное поле?')

    def __str__(self):
        return f'{self.get_field_type_display()} ({self.field_placeholder})'


class FAQ(models.Model):
    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'

    is_active = models.BooleanField(default=True)
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class StudentsReviews(models.Model):
    class Meta:
        verbose_name = 'Отзыв ученика'
        verbose_name_plural = 'Отзывы учеников'

    is_active = models.BooleanField(default=True)
    author = models.TextField()
    review_text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author

