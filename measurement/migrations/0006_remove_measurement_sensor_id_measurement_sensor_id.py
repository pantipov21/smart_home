# Generated by Django 4.0.4 on 2022-05-25 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0005_remove_measurement_sensor_id_measurement_sensor_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='sensor_id',
        ),
        migrations.AddField(
            model_name='measurement',
            name='sensor_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sensors', to='measurement.sensor'),
            preserve_default=False,
        ),
    ]
