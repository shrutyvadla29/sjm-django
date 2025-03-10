# Generated by Django 5.1.4 on 2025-03-03 15:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_delete_scores"),
    ]

    operations = [
        migrations.CreateModel(
            name="Scores",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("score", models.IntegerField()),
                ("remarks", models.TextField(blank=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.user"
                    ),
                ),
            ],
        ),
    ]
