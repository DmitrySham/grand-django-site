# Generated by Django 2.2 on 2019-05-28 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_applyrequest_is_approved'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('order_index',), 'verbose_name': 'Курс', 'verbose_name_plural': 'Курсы'},
        ),
    ]
