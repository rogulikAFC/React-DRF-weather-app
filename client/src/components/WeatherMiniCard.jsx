export default function WeatherMiniCard({weather}) {
    const toTitle = string => string[0].toUpperCase() + string.substring(1)

    return (
        <div className="weather-mini-card card__weather-mini-card" id={weather.id}>
            <div className="weather-mini-card__header">
                <h3 className="weather-mini-card__title"> {weather.time} </h3>
            </div>

            <div className=" weather-mini-card__temperature">
                <strong className="weather-mini-card__fact-temperature"> {weather.temperature.temperature > 0 ? '+' : null}{weather.temperature.temperature}ºC </strong>
                <p className="weather-mini-card__feels-like-temperature"> {weather.temperature.feels_like}ºC </p>
            </div>

            <figure className="weather-mini-card__type">
                <img src={weather.icon_url} alt="" className="weather-mini-card__img-type" />
                <figcaption className="weather-mini-card__type-caption"> { toTitle(weather.type) } </figcaption>
            </figure>
        </div>
    )
}