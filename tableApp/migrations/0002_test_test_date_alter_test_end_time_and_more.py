# Generated by Django 4.0.5 on 2022-10-11 15:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tableApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='test_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='시험날짜'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='test',
            name='end_time',
            field=models.TimeField(verbose_name='종료시간'),
        ),
        migrations.AlterField(
            model_name='test',
            name='start_time',
            field=models.TimeField(verbose_name='시작시간'),
        ),
    ]
