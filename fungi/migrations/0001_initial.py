# Generated by Django 4.2.6 on 2023-10-22 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Fungi",
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
                ("french_name", models.CharField(max_length=200)),
                ("latin_name", models.CharField(max_length=200)),
                ("comestible", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Genre",
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
                ("name", models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="FungiImage",
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
                ("image", models.ImageField(upload_to="fungi_images/")),
                (
                    "fungi",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="fungi.fungi",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="fungi",
            name="genre",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="fungi.genre"
            ),
        ),
    ]