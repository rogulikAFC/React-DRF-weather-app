import { useEffect, useState } from "react"
import { useParams } from "react-router-dom"
import Card from "../components/Card"
import WeatherMiniCard from "../components/WeatherMiniCard"

export default function ForecastDay() {
    let [forecasts, setForecasts] = useState([])
    let [isLoading, setIsLoading] = useState(false)
    let {cityId} = useParams()

    // const dateToString = date => `${date.getFullYear()}-${date.getMonth().toString().length === 1? '0' : null}${date.getMonth() + 1}-${date.getDate().toString().length === 1? '0' : ''}${date.getDate()}`
    const dateToString = date => `${date.getDate().toString().length === 1? '0' : ''}${date.getDate()}-${date.getMonth().toString().length === 1? '0' : null}${date.getMonth() + 1}-${date.getFullYear()}`

    const fetchForecast = async () => {
        setIsLoading(true)
        let today = new Date()
        today = dateToString(today)
        
        let response = await fetch(
            `http://127.0.0.1:8000/api/forecast/${cityId}/${today}`
        )

        let json = await response.json()
        setForecasts(json)
        setIsLoading(false)
    }

    useEffect(() => {
        fetchForecast()
    }, [])

    useEffect(() => {
        fetchForecast()
    }, [cityId])

    return (
        <Card elName="main__card" modName="card_white" title="Today weather">
            {isLoading? <h2> Loading... </h2> : null}
            {forecasts.length > 0 ? forecasts.map(forecast => <WeatherMiniCard weather={forecast} key={forecast.id}/>) : <strong> Service can't provide weather in this region </strong>}
        </Card>
    )
}