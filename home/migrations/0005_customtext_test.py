# Generated by Django 2.2.12 on 2020-04-27 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_customtext_ttesttt'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtext',
            name='test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customtext_test', to=settings.AUTH_USER_MODEL),
        ),
    ]
