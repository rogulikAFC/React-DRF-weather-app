import datetime
from rest_framework import serializers
from .models import Forecast, City


class ForecastSerializer(serializers.ModelSerializer):
    temperature = serializers.SerializerMethodField(
        'get_temperature'
    )
    wind = serializers.SerializerMethodField(
        'get_wind'
    )
    type = serializers.SerializerMethodField(
        'get_type'
    )
    date_detail = serializers.SerializerMethodField(
        'get_date_detail'
    )
    time = serializers.SerializerMethodField(
        'get_time'
    )
    day_part = serializers.SerializerMethodField(
        'get_day_part'
    )
    icon_url = serializers.CharField(
        source='get_icon_path'
    )

    class Meta:
        model = Forecast
        fields = [
            'id', 'date_detail', 'time',
            'temperature', 'pressure',
            'air_humidity', 'wind', 'UV_index',
            'type', 'day_part', 'icon_url'
        ]

    def get_temperature(self, obj: Forecast) -> dict:
        return {
            'temperature': obj.temperature,
            'feels_like': obj.feels_like
        }
    
    def get_wind(self, obj: Forecast) -> dict:
        return {
            'speed': obj.wind_speed,
            'blowing': obj.wind_blowing
        }
    
    def get_type(self, obj: Forecast) -> str:
        return obj.type.title
    
    def get_date_detail(self, obj: Forecast) -> dict:
        WEEKDAYS = (
            (1, 'Mon.', 'Monday'),
            (2, 'Tue.', 'Tuesday'),
            (3, 'Wed.', 'Wednesday'),
            (4, 'Thu.', 'Thursday'),
            (5, 'Fri.', 'Friday'),
            (6, 'Sat.', 'Saturday'),
            (7, 'Sun.', 'Sunday')
        )

        weekday_count = datetime.date.isoweekday(
            obj.date
        )
        weekday_detail = WEEKDAYS[weekday_count - 1]

        return {
            'date': obj.date,
            'weekday_full': weekday_detail[2],
            'weekday_short': weekday_detail[1],
            'isoweekday': weekday_count
        }
    
    def get_time(self, obj: Forecast) -> str:
        return datetime.time.strftime(obj.time, '%H:%M')
    
    def get_day_part(self, obj: Forecast) -> str:
        if obj.is_day:
            return 'day'
        
        return 'night'
    

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'title']
