# Generated by Django 2.2 on 2020-12-13 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0017_license'),
    ]

    operations = [
        migrations.AddField(
            model_name='license',
            name='title',
            field=models.CharField(default='', max_length=255, verbose_name='Название'),
        ),
    ]
