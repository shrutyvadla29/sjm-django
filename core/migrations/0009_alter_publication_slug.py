# Generated by Django 5.1.4 on 2025-03-03 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_publication_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="publication",
            name="slug",
            field=models.SlugField(
                blank=True, default="", editable=False, max_length=300, unique=True
            ),
        ),
    ]
