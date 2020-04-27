# Generated by Django 2.2.12 on 2020-04-27 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_load_initial_data"),
    ]

    operations = [
        migrations.AddField(
            model_name="customtext",
            name="ttestt",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="customtext_ttestt",
                to="home.CustomText",
            ),
        ),
    ]
