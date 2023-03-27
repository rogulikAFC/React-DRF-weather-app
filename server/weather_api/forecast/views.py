import datetime

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import generics, filters, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import City
from .serializers import ForecastSerializer, CitySerializer


class ForecastList(generics.ListAPIView):
    serializer_class = ForecastSerializer

    def get_queryset(self) -> list:
        url_params = self.kwargs

        city_code = url_params['city_code']
        city = get_object_or_404(City, pk=city_code)

        date = datetime.datetime.strptime(url_params['date'], '%d-%m-%Y')

        # end date is last date in range of forecasts
        end_date = url_params.get('end_date')

        if end_date:
            end_date = datetime.datetime.strptime(end_date, '%d-%m-%Y')

        # forecast for n next days
        next_count = url_params.get('next_count')

        # getting end date if next_count given
        if next_count:
            delta = datetime.timedelta(days=next_count)
            end_date = date + delta

        # filtering by range of dates
        if end_date:
            return city.forecast.filter(
                date__range=[date, end_date]
            ).order_by('time')
        
        # if no end_date. Forecast for one day
        return city.forecast.filter(
            date=date
        ).order_by('time')


class CityList(generics.ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


@api_view(['GET'])
def get_city_id(request, title):
    city = get_object_or_404(City, title__iexact=title)

    return Response({'id': city.id}, status=status.HTTP_200_OK)
