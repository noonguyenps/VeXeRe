# Generated by Django 4.1.3 on 2022-11-30 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0008_garage_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
