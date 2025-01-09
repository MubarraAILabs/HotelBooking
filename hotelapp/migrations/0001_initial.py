# Generated by Django 5.1.4 on 2024-12-30 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hotel",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("address", models.TextField()),
                ("type", models.CharField(max_length=100)),
                ("rating", models.FloatField()),
                ("contact", models.CharField(max_length=15)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="hotel_images/"),
                ),
            ],
        ),
    ]
