# Generated by Django 4.1.7 on 2023-03-27 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0002_forecast_is_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='weathertype',
            name='day_image',
            field=models.ImageField(default=None, null=True, upload_to='images/weather_icons/day/'),
        ),
        migrations.AddField(
            model_name='weathertype',
            name='night_image',
            field=models.ImageField(default=None, null=True, upload_to='images/weather_icons/night/'),
        ),
    ]