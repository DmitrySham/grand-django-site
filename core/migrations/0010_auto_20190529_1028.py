# Generated by Django 2.2 on 2019-05-29 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20190527_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='index_page_text',
            field=models.TextField(blank=True, null=True, verbose_name='Текст на главной странице'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='news_header_image',
            field=models.FileField(blank=True, null=True, upload_to='blog/headers/', verbose_name='Изображение на странице новостей'),
        ),
    ]
