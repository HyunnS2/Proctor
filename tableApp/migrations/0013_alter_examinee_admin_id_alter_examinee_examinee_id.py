# Generated by Django 4.0.5 on 2022-10-25 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tableApp', '0012_remove_examinee_examinee_name_examinee_examinee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examinee',
            name='admin_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='admin_id', to=settings.AUTH_USER_MODEL, verbose_name='감독관id'),
        ),
        migrations.AlterField(
            model_name='examinee',
            name='examinee_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='examinee_id', to=settings.AUTH_USER_MODEL, verbose_name='응시자 아이디'),
        ),
    ]
