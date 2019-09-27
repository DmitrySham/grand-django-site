# Generated by Django 2.2 on 2019-09-24 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0012_course_share_links'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.TextField(verbose_name='Дата начала занятий')),
                ('start_hour', models.TimeField(verbose_name='Время начала занятий')),
                ('finish_hour', models.TimeField(verbose_name='Время конца занятий')),
                ('days', models.TextField(verbose_name='Дни недель')),
                ('duration', models.TextField(verbose_name='Продолжительность')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписание',
            },
        ),
        migrations.RemoveField(
            model_name='courseactiondateobject',
            name='course',
        ),
        migrations.RemoveField(
            model_name='course',
            name='schedule',
        ),
        migrations.DeleteModel(
            name='ApplyRequest',
        ),
        migrations.DeleteModel(
            name='CourseActionDateObject',
        ),
        migrations.DeleteModel(
            name='Educations',
        ),
        migrations.AddField(
            model_name='schedule',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Course', verbose_name='Курс'),
        ),
    ]