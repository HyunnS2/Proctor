# Generated by Django 4.0.5 on 2022-10-22 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableApp', '0010_rename_in_room_examinee_entry_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examinee',
            name='test_id',
            field=models.IntegerField(verbose_name='시험 코드'),
        ),
    ]
