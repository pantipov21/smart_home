# Generated by Django 4.0.4 on 2022-05-26 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0008_rename_sensor_id_measurement_sensor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='sensor',
            new_name='sensor_id',
        ),
    ]