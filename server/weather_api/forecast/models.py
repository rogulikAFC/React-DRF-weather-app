from uuid import uuid4
from os import path

from django.db import models
from django.dispatch import receiver


class City(models.Model):
    id = models.UUIDField(
        default=uuid4, primary_key=True
    )
    title = models.CharField(
        max_length=32, null=False
    )
    forecast = models.ManyToManyField(to='Forecast')

    def __str__(self) -> str:
        return f'{self.title} ({self.id})'
        

WIND_BLOWING_CHOICES = (
    ('south', 'south'),
    ('north', 'north'),
    ('east', 'east'),
    ('west', 'west'),
    ('southeast', 'southeast'),
    ('southwest', 'southwest'),
    ('northeast', 'northeast'),
    ('northwest', 'northwest')
)

class Forecast(models.Model):
    id = models.UUIDField(
        default=uuid4, primary_key=True
    )
    date = models.DateField(default=None)
    time = models.TimeField(default=None)
    type = models.ForeignKey(
        'WeatherType', on_delete=models.SET_NULL,
        null=True
    )
    temperature = models.IntegerField(default=None)
    feels_like = models.IntegerField(default=None)
    pressure = models.IntegerField(default=None)
    air_humidity = models.IntegerField(default=None)
    wind_speed = models.IntegerField(default=None)
    wind_blowing = models.CharField(
        choices=WIND_BLOWING_CHOICES,
        default=None,
        max_length=32
    )
    UV_index = models.IntegerField(default=None)
    is_day = models.BooleanField(default=True)

    def get_city(self) -> str:
        try:
            return City.objects.get(
                forecast__in=[self]
            ).title
        
        except:
            return
        
    def get_icon_path(self) -> str:
        template = 'http://127.0.0.1:8000/media/images/weather_icons/{day_part}/{basename}'

        if self.is_day:
            return template.format(
                basename=path.basename(self.type.day_image.name),
                day_part='day'
            )
        
        return template.format(
            basename=path.basename(self.type.night_image.name),
            day_part='night'
        )

    def __str__(self) -> str:
        return f'Forecast to {self.date} {self.time} {f"in {self.get_city()}" if self.get_city() else ""}'


class WeatherType(models.Model):
    id = models.UUIDField(
        default=uuid4, primary_key=True
    )
    title = models.CharField(
        default=None, max_length=32
    )
    night_image = models.ImageField(
        default=None, null=True, upload_to='images/weather_icons/night/'
    )
    day_image = models.ImageField(
        default=None, null=True, upload_to='images/weather_icons/day/'
    )

    def __str__(self) -> str:
        return self.title


@receiver(models.signals.pre_delete, sender=WeatherType)
def handle_weather_type_delete(sender: WeatherType, instance: WeatherType, **kwargs):
    try:
        instance.day_image.delete(False)
        instance.night_image.delete(False)

    except:
        return
