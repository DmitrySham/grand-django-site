# Generated by Django 2.2 on 2019-04-29 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190429_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='description',
            field=models.TextField(help_text='HTML теги разрешены', verbose_name='Описание'),
        ),
    ]
