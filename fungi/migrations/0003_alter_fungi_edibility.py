# Generated by Django 4.2.6 on 2023-10-22 19:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fungi", "0002_remove_fungi_comestible_fungi_edibility_fungi_smell"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fungi",
            name="edibility",
            field=models.CharField(
                choices=[
                    ("COM", "Comestible"),
                    ("NI", "Not Interesting"),
                    ("TOX", "Toxic"),
                    ("MOR", "Mortal"),
                ],
                default="NI",
                max_length=3,
            ),
        ),
    ]
