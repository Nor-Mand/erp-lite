# Generated by Django 4.1.5 on 2023-01-20 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounting", "0003_alter_taxes_account_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Currency",
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
                ("name", models.CharField(max_length=220)),
                ("symbol", models.CharField(max_length=5)),
                ("abbrev", models.CharField(max_length=5)),
                ("date", models.DateField()),
                ("rate", models.IntegerField()),
                ("status", models.BooleanField()),
            ],
        ),
    ]
