# Generated by Django 2.2 on 2023-01-13 10:59

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0019_educators'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educators',
            name='full_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Полное описание'),
        ),
    ]
