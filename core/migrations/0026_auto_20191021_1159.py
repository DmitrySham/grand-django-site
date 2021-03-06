# Generated by Django 2.2 on 2019-10-21 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_sitesettings_icon_heading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='icon_heading',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название раздела с иконками'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='why_choose_us',
            field=models.TextField(blank=True, null=True, verbose_name='Текст на главной странице'),
        ),
    ]
