# Generated by Django 2.2 on 2025-03-25 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0032_auto_20250321_1553'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscriptionplancharacteristics',
            options={'ordering': ('order_index',), 'verbose_name': 'Характеристика тарифа', 'verbose_name_plural': 'Характеристики тарифов'},
        ),
        migrations.AddField(
            model_name='subscriptionplancharacteristics',
            name='order_index',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
