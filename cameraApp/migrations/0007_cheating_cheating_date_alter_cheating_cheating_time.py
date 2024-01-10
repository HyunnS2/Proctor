# Generated by Django 4.0.5 on 2022-10-31 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cameraApp', '0006_remove_cheating_admin_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='cheating',
            name='cheating_date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='날짜'),
        ),
        migrations.AlterField(
            model_name='cheating',
            name='cheating_time',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='시간'),
        ),
    ]
