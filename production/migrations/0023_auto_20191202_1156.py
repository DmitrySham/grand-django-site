# Generated by Django 2.2 on 2019-12-02 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0022_auto_20191202_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onec',
            name='slug',
            field=models.CharField(max_length=255, unique=True, verbose_name='SLUG'),
        ),
        migrations.AlterField(
            model_name='onlinecashbox',
            name='slug',
            field=models.CharField(max_length=255, unique=True, verbose_name='SLUG'),
        ),
    ]
