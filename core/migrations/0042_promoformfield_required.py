# Generated by Django 2.2 on 2020-11-29 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_promoformbuilder_promoformfield_promovisitor'),
    ]

    operations = [
        migrations.AddField(
            model_name='promoformfield',
            name='required',
            field=models.BooleanField(default=False, verbose_name='Обязательное поле?'),
        ),
    ]
