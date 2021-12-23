# Generated by Django 3.2.9 on 2021-12-11 16:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="device",
            name="location",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="devices",
                to="core.location",
            ),
        ),
        migrations.AlterField(
            model_name="sensor",
            name="device",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sensors",
                to="core.device",
            ),
        ),
        migrations.AlterField(
            model_name="sensorrecord",
            name="location",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="records",
                to="core.location",
            ),
        ),
        migrations.AlterField(
            model_name="sensorrecord",
            name="sensor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="records",
                to="core.sensor",
            ),
        ),
    ]
