# Generated by Django 2.2 on 2019-06-14 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0008_course_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyrequest',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='applyrequest',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия'),
        ),
        migrations.AddField(
            model_name='applyrequest',
            name='middle_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Отчество'),
        ),
    ]
