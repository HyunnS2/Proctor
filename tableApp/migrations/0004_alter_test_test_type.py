# Generated by Django 4.0.5 on 2022-10-12 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableApp', '0003_alter_test_test_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='test_type',
            field=models.BooleanField(default=False, verbose_name='기능 추가(아이트래킹,각도'),
        ),
    ]