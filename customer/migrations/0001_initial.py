# Generated by Django 5.0.4 on 2024-04-17 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=50)),
                ("birth_date", models.DateField()),
                ("email", models.EmailField(max_length=254)),
                ("area_code", models.CharField(max_length=3)),
                ("phone_number", models.CharField(max_length=9)),
                ("address", models.CharField(max_length=50)),
                ("neighborhood", models.CharField(max_length=30)),
                ("city", models.CharField(max_length=30)),
                ("state", models.CharField(max_length=2)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                ("active", models.BooleanField(default=True)),
            ],
            options={
                "db_table": "customer",
            },
        ),
    ]
