# Generated by Django 2.2 on 2023-01-13 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0023_auto_20230113_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='educators',
            name='slug',
            field=models.CharField(max_length=255, null=True, verbose_name='SLUG'),
        ),
    ]