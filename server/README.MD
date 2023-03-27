# API
----
## Cities
**api/forecast/cities** returns list of cities. In app, this endpoint using to filter cities.

### Response example

`[
    {
        "id": "7d6f9f0b-4fe8-412b-8c86-21debe6f3cb6",
        "title": "Samara"
    },
    {
        "id": "93d99505-0a12-44f9-b303-6e222ee24fea",
        "title": "Moskow"
    },
    {
        "id": "9dc53e84-19f9-45cc-b2da-98e0a45ba05b",
        "title": "Saint Petersburg"
    }
]`

**api/forecast/get-city-id/<str:title>** gets city by *title* and returns thats id.

### Response example

`{
    "id": "7d6f9f0b-4fe8-412b-8c86-21debe6f3cb6"
}`

----
## Weather
### Response example:

`[{
    "id": "7a7233fe-9d22-4670-9b7d-b09ea6321371",
    "date_detail": {
        "date": "2023-03-20",
        "weekday_full": "Monday",
        "weekday_short": "Mon.",
        "isoweekday": 1
    },
    "time": "05:30",
    "temperature": {
        "temperature": 3,
        "feels_like": -1
    },
    "pressure": 720,
    "air_humidity": 78,
    "wind": {
        "speed": 4,
        "blowing": "southeast"
    },
    "UV_index": 1,
    "type": "clear",
    "day_part": "day",
    "icon_url": "http://127.0.0.1:8000/media/images/weather_icons/day/day_clear.png"
},]`

**api/forecast/<uuid:city_code>/<str:date>** returns forecast to *date*.

**api/forecast/<uuid:city_code>/<str:date>/<str:end_date>** returns forecast from *date* to *end_date*.

**api/forecast/<uuid:city_code>/<str:date>/next/<int:next_count>** returns forecast to *next_count* dates starting from *date*.