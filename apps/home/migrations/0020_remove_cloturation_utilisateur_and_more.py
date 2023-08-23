# Generated by Django 4.2.3 on 2023-08-15 07:43

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0019_remove_charge_code_entity_alter_charge_insert_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cloturation',
            name='utilisateur',
        ),
        migrations.AlterField(
            model_name='charge',
            name='insert_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 15, 7, 43, 55, 968746, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='CloturationUSer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('SemaineClose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.semaine')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
