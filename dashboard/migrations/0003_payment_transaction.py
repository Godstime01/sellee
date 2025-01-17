# Generated by Django 5.0.6 on 2024-05-18 01:05

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0002_coin"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
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
                (
                    "_id",
                    models.UUIDField(
                        default=uuid.UUID("93e559be-96d8-4960-9626-4cd98b01c032")
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=14)),
                ("date", models.DateField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("paid", "paid"),
                            ("pending", "pending"),
                            ("processing", "processing"),
                            ("cancelled", "cancelled"),
                            ("successful", "successful"),
                        ],
                        max_length=15,
                    ),
                ),
                (
                    "seller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
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
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("paid", "paid"),
                            ("pending", "pending"),
                            ("processing", "processing"),
                            ("cancelled", "cancelled"),
                            ("successful", "successful"),
                        ],
                        max_length=15,
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=14)),
                ("date", models.DateField()),
                (
                    "payment_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="dashboard.payment",
                    ),
                ),
                (
                    "seller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
