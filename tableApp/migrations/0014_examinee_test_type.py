# Generated by Django 4.0.5 on 2022-10-25 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableApp', '0013_alter_examinee_admin_id_alter_examinee_examinee_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='examinee',
            name='test_type',
            field=models.CharField(db_column='test_type', default='paper', max_length=10),
        ),
    ]
