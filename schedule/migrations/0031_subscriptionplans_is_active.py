# Generated by Django 2.2 on 2025-03-21 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0030_auto_20250321_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptionplans',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
