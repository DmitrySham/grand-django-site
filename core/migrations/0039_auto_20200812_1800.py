# Generated by Django 2.2 on 2020-08-12 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_auto_20200812_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='index_page_h1_text',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='h1 тег на главной странице'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='one_c_h1_text',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='h1 тег на странице  "1C"'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='online_cash_box_h1_text',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='h1 тег на странице "Онлайн Кассы"'),
        ),
    ]