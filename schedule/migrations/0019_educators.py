# Generated by Django 2.2 on 2023-01-13 10:47

import core.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0018_license_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Educators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно?')),
                ('order_index', models.PositiveIntegerField(default=0, verbose_name='Порядковый номер')),
                ('name', models.TextField(verbose_name='ФИО')),
                ('short_description', models.TextField(blank=True, null=True, verbose_name='Краткое описание')),
                ('full_description', models.TextField(blank=True, null=True, verbose_name='Полное описание')),
                ('photo', models.ImageField(upload_to=core.utils.SetUniqueName('educators'), verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
                'ordering': ('order_index',),
            },
        ),
    ]
