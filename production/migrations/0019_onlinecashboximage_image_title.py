# Generated by Django 2.2 on 2019-11-16 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0018_auto_20191116_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlinecashboximage',
            name='image_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Атрибут alt'),
        ),
    ]
