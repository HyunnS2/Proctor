# Generated by Django 4.0.5 on 2022-11-01 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cameraApp', '0008_remove_cheating_cheating_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cheating',
            name='test_name',
            field=models.CharField(db_column='testname', default='테스트', max_length=128, verbose_name='시험 과목'),
        ),
    ]
