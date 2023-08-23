# Generated by Django 4.2.3 on 2023-07-31 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=3)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('foreverybody', models.IntegerField(db_column='ForEverybody', db_comment='Elle permet de signifier si une activitÚ concerne une seule personne ou pas. 0 si elle concerne une seule personne et 1 sinon')),
            ],
        ),
        migrations.CreateModel(
            name='Entite',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('localization', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('racine', models.IntegerField()),
                ('parent', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Semaine',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('year', models.IntegerField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('closed', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EntityUSer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.entite')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EntityActivity',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('debut', models.DateTimeField()),
                ('fin', models.DateTimeField()),
                ('code_activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.activity')),
                ('code_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Charge',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('charge', models.FloatField()),
                ('insert_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField()),
                ('code_activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.activity')),
                ('code_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.entite')),
                ('id_semaine', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.semaine')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('action', models.CharField(max_length=1)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]