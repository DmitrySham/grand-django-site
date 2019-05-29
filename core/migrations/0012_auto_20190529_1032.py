# Generated by Django 2.2 on 2019-05-29 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20190529_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='electronic_signature_header_image',
            field=models.FileField(blank=True, null=True, upload_to='electronic-signature/headers/', verbose_name='Изображение на странице "Электронные подписи"'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='grand_smeta_header_image',
            field=models.FileField(blank=True, null=True, upload_to='grand-smeta/headers/', verbose_name='Изображение на странице "Гранд Смета"'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='online_cash_box_header_image',
            field=models.FileField(blank=True, null=True, upload_to='online-cahs-box/headers/', verbose_name='Изображение на странице "Онлайн Кассы"'),
        ),
    ]
