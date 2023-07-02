# Generated by Django 4.1.5 on 2023-07-02 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounting", "0007_alter_chartofaccounts_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="chartofaccounts",
            name="status",
            field=models.CharField(
                choices=[("SV", "Saved"), ("PB", "Published")],
                default="SV",
                max_length=2,
            ),
        ),
        migrations.CreateModel(
            name="JournalEntries",
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
                ("date", models.DateField()),
                ("reference", models.CharField(max_length=250)),
                ("debit", models.DecimalField(decimal_places=2, max_digits=10)),
                ("credit", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "account_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounting.chartofaccounts",
                    ),
                ),
            ],
        ),
    ]
