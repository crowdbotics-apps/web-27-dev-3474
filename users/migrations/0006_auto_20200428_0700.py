# Generated by Django 2.2.12 on 2020-04-28 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200427_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='fcgv',
        ),
        migrations.RemoveField(
            model_name='user',
            name='fsrtfhgv',
        ),
    ]
