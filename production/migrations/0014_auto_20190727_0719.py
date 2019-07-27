# Generated by Django 2.2 on 2019-07-27 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0013_onec_share_links'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineCashboxCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_index', models.PositiveIntegerField(default=0, verbose_name='Порядковый номер')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категорию',
                'verbose_name_plural': 'Категории онлайн касс',
                'ordering': ('order_index',),
            },
        ),
        migrations.AddField(
            model_name='onlinecashbox',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='production.OnlineCashboxCategory', verbose_name='Категория'),
        ),
    ]
