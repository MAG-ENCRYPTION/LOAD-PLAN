# Generated by Django 4.2.3 on 2023-08-15 15:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_remove_cloturation_utilisateur_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectFermé',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nomProjet', models.CharField(max_length=100)),
                ('dateFemeture', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='charge',
            name='insert_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 15, 15, 4, 29, 541926, tzinfo=datetime.timezone.utc)),
        ),
    ]
