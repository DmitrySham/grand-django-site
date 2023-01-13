# Generated by Django 2.2 on 2023-01-13 11:58

import core.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0022_auto_20230113_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educators',
            name='photo',
            field=models.ImageField(help_text='Желаемый размер изображения: 348x348', upload_to=core.utils.SetUniqueName('educators'), verbose_name='Фотография'),
        ),
    ]