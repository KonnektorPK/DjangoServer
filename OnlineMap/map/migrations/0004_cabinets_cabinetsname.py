# Generated by Django 4.2.18 on 2025-01-19 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("map", "0003_remove_cabinets_cabinetappointment_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="cabinets",
            name="cabinetsName",
            field=models.CharField(default="1", max_length=6, verbose_name="name"),
        ),
    ]
