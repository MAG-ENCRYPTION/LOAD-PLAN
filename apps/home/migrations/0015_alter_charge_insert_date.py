# Generated by Django 4.2.3 on 2023-08-02 03:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_entityactivity_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charge',
            name='insert_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 2, 3, 5, 44, 761698, tzinfo=datetime.timezone.utc)),
        ),
    ]
