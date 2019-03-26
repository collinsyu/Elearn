# Generated by Django 2.0.13 on 2019-03-26 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoapp', '0002_auto_20190326_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='cover',
            field=models.ImageField(max_length=200, upload_to='upload/cover/%Y%m%d', verbose_name='课程封面'),
        ),
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(max_length=200, upload_to='upload/video/%Y%m%d', verbose_name='视频'),
        ),
    ]
