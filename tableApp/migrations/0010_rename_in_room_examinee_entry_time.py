# Generated by Django 4.0.5 on 2022-10-22 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tableApp', '0009_alter_examinee_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examinee',
            old_name='in_Room',
            new_name='entry_time',
        ),
    ]