from django.contrib import admin
from .models import *

admin.site.register(WeatherType)

@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'get_city', 'date',
        'time', 'get_day_part', 'get_temperature',
        'pressure', 'get_type_title', 'UV_index',
        'get_wind'
    ]
    search_fields = ['date', 'time']
    ordering = ['-time']

    def get_type_title(self, obj: Forecast) -> str:
        return obj.type.title
    
    get_type_title.short_description = 'type'
    
    def get_temperature(self, obj: Forecast) -> str:
        temp = obj.temperature
        feels_like = obj.feels_like

        return f"{'+' if temp > 0 else ''}{temp}°C, feels like {'+' if feels_like > 0 else ''}{feels_like}°C"
    
    get_temperature.short_description = 'temperature'

    def get_wind(self, obj: Forecast) -> str:
        speed = obj.wind_speed
        blowing = obj.wind_blowing

        return f'{speed} m/s, {blowing}'
    
    get_wind.short_description = 'wind'

    def get_city(self, obj: Forecast) -> str:
        city = City.objects.get(
            forecast__in=[obj]
        )

        return city.title
    
    get_city.short_description = 'city'

    def get_day_part(self, obj: Forecast) -> str:
        if obj.is_day:
            return 'day'
        
        return 'night'
    
    get_day_part.short_description = 'day part'


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title', 'id']
