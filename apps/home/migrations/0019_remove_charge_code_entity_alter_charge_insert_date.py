# Generated by Django 4.2.3 on 2023-08-04 11:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_remove_charge_cloture_remove_cloturation_estclose_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charge',
            name='code_entity',
        ),
        migrations.AlterField(
            model_name='charge',
            name='insert_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 4, 11, 57, 13, 301434, tzinfo=datetime.timezone.utc)),
        ),
    ]