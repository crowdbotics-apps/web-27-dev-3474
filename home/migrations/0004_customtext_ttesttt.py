# Generated by Django 2.2.12 on 2020-04-27 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_customtext_ttestt"),
    ]

    operations = [
        migrations.AddField(
            model_name="customtext",
            name="ttesttt",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="customtext_ttesttt",
                to="home.CustomText",
            ),
        ),
    ]
