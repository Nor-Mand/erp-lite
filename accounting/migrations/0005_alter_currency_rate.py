# Generated by Django 4.1.5 on 2023-01-20 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounting", "0004_currency"),
    ]

    operations = [
        migrations.AlterField(
            model_name="currency",
            name="rate",
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]