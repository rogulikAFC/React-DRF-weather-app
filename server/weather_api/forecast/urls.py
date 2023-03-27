from django.urls import path
from .views import *


urlpatterns = [
    path('<uuid:city_code>/<str:date>', ForecastList.as_view(),  name='weather_forecast'),
    path('<uuid:city_code>/<str:date>/<str:end_date>', ForecastList.as_view(),  name='weather_forecast_date_range'),
    path('<uuid:city_code>/<str:date>/next/<int:next_count>', ForecastList.as_view(),  name='weather_forecast_to_next_n'),
    
    path('cities', CityList.as_view(), name='get_all_cities'),
    path('get-city-id/<str:title>', get_city_id, name='get_city_id')
]
