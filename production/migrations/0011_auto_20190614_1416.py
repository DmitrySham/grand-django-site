# Generated by Django 2.2 on 2019-06-14 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0010_auto_20190613_1437'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='onec',
            options={'ordering': ('order_index',), 'verbose_name': '1С', 'verbose_name_plural': '1С'},
        ),
        migrations.AlterModelOptions(
            name='onlinecashbox',
            options={'ordering': ('order_index',), 'verbose_name': 'Онлайн касса', 'verbose_name_plural': 'Онлайн кассы'},
        ),
        migrations.AddField(
            model_name='onec',
            name='order_index',
            field=models.PositiveIntegerField(default=0, verbose_name='Порядковый номер'),
        ),
        migrations.AddField(
            model_name='onlinecashbox',
            name='order_index',
            field=models.PositiveIntegerField(default=0, verbose_name='Порядковый номер'),
        ),
    ]
