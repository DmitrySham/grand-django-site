# Generated by Django 2.2 on 2019-09-26 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0016_onecimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onec',
            name='price',
        ),
    ]
