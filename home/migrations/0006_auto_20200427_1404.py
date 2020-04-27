# Generated by Django 2.2.12 on 2020-04-27 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_customtext_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='czvfc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='homepage_czvfc', to='home.CustomText'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='ghcgv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='homepage_ghcgv', to='home.HomePage'),
        ),
    ]