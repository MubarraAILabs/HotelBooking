# Generated by Django 5.1.4 on 2024-12-31 06:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customerapp", "0002_alter_customer_email"),
        ("hotelapp", "0005_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Booking",
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
                ("no_of_people", models.IntegerField()),
                ("check_in", models.DateTimeField()),
                ("check_out", models.DateTimeField()),
                ("total_price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customerapp.customer",
                    ),
                ),
                (
                    "hotel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="hotelapp.hotel"
                    ),
                ),
                (
                    "room_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hotelapp.category",
                    ),
                ),
            ],
        ),
    ]
