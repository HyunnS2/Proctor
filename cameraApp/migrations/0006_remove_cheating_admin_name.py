# Generated by Django 4.0.5 on 2022-10-31 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cameraApp', '0005_alter_cheating_cheating_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cheating',
            name='admin_name',
        ),
    ]
