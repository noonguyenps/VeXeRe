# Generated by Django 4.1.3 on 2022-11-28 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0004_garage_deleted_manager_garage_id_ticket_schedule_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='departure_time',
            field=models.DateTimeField(),
        ),
    ]
