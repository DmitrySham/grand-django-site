# Generated by Django 2.2 on 2019-09-26 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0013_auto_20190924_0840'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='cost',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='have_own_cost',
            field=models.BooleanField(default=False, verbose_name='Другая цена?'),
        ),
    ]
