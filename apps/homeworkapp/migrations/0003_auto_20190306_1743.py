# Generated by Django 2.0.6 on 2019-03-06 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeworkapp', '0002_auto_20190306_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='boolf',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='boolt',
        ),
    ]
