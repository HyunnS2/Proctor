# Generated by Django 4.0.5 on 2022-11-06 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cameraApp', '0010_alter_cheating_admin_id_alter_cheating_examinee_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cheating',
            name='examinee_name',
            field=models.CharField(default='name', max_length=24, verbose_name='응시자이름'),
        ),
    ]