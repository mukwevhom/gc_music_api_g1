# Generated by Django 4.1.7 on 2023-03-28 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Song",
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
                ("songname", models.CharField(max_length=255)),
                ("songartist", models.CharField(max_length=255)),
                ("songimg", models.CharField(max_length=255)),
            ],
        ),
    ]
