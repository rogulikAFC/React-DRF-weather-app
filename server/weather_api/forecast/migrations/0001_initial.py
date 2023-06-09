# Generated by Django 4.1.7 on 2023-03-20 05:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(default=None, max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('date', models.DateField(default=None)),
                ('time', models.TimeField(default=None)),
                ('temperature', models.IntegerField(default=None)),
                ('feels_like', models.IntegerField(default=None)),
                ('pressure', models.IntegerField(default=None)),
                ('air_humidity', models.IntegerField(default=None)),
                ('wind_speed', models.IntegerField(default=None)),
                ('wind_blowing', models.CharField(choices=[('south', 'south'), ('north', 'north'), ('east', 'east'), ('west', 'west'), ('southeast', 'southeast'), ('southwest', 'southwest'), ('northeast', 'northeast'), ('northwest', 'northwest')], default=None, max_length=32)),
                ('UV_index', models.IntegerField(default=None)),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='forecast.weathertype')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('forecast', models.ManyToManyField(to='forecast.forecast')),
            ],
        ),
    ]
