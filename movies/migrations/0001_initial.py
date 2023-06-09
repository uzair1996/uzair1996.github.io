# Generated by Django 4.1.7 on 2023-03-23 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Moviesss",
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
                ("movie_title", models.CharField(max_length=150)),
                ("release_year", models.IntegerField()),
                ("director", models.CharField(max_length=150)),
                ("movie_plot", models.TextField()),
            ],
        ),
    ]
