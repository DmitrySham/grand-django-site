# Generated by Django 2.2 on 2019-11-19 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0020_onecimage_image_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='onec',
            name='image_title_alt',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Атрибут alt'),
        ),
    ]