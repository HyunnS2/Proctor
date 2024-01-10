# Generated by Django 4.0.5 on 2022-11-06 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('postApp', '0003_alter_fileupload_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileupload',
            name='examinee_id',
        ),
        migrations.AddField(
            model_name='fileupload',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
    ]