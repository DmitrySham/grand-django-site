# Generated by Django 2.2 on 2019-11-19 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20191116_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='grandsmeta',
            name='art_alt',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Атрибут alt'),
        ),
    ]