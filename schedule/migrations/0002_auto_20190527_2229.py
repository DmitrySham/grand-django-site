# Generated by Django 2.2 on 2019-05-27 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('order_index',), 'verbose_name': 'Курс', 'verbose_name_plural': 'Учебный центр'},
        ),
        migrations.AddField(
            model_name='course',
            name='order_index',
            field=models.PositiveIntegerField(default=0, verbose_name='Порядок'),
        ),
    ]