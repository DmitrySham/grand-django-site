# Generated by Django 2.2 on 2023-01-13 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0020_auto_20230113_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='educators',
            name='photo_alt',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Значение атрибута alt'),
        ),
    ]
