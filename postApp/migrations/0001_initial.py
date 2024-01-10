# Generated by Django 4.0.5 on 2022-11-06 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examinee_id', models.CharField(max_length=40, null=True)),
                ('test_name', models.CharField(max_length=40, null=True)),
                ('content', models.TextField()),
                ('imgfile', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
