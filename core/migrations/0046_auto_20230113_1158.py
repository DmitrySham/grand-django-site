# Generated by Django 2.2 on 2023-01-13 11:58

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_sitesettings_educators_h1_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='educators_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст на странице "Преподаватели"'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='educators_h1_text',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='<h1> тег на странице "Преподаватели"'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='one_c_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст в 1С'),
        ),
    ]
