# Generated by Django 2.2 on 2020-02-20 16:45

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_privacypolicy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privacypolicy',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
