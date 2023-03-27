import { createRef, useEffect, useState } from "react"
import { useNavigate } from "react-router-dom"

export default function CitySearchForm() {
    const [cityName, setCityName] = useState()
    const [cityOptions, setCityOptions] = useState([])
    const [error, setError] = useState()
    // const navigate = useNavigate()

    const navigate = useNavigate()

    const handleNameChange = e => {
        setCityName(e.target.value)
    }

    const updateDatalist = async () => {
        let response = await fetch(`http://127.0.0.1:8000/api/forecast/cities?search=${cityName}`)
        let json = await response.json()
        setCityOptions(json)
    }

    useEffect(() => {
        updateDatalist()
    }, [cityName])

    const handleSubmit = async e => {
        e.preventDefault()

        let response = await fetch(`http://127.0.0.1:8000/api/forecast/get-city-id/${cityName}`)

        if (!response.ok) {
            setError('City is not found')

            return
        }

        let json = await response.json()
        console.log(json.id)

        // return navigate(`/forecast/${json.id}`)
        // return redirect(`/forecast/${json.id}`)
        navigate(`/forecast/${json.id}`)
    }

    return (
        <form className="form header__form form_horizontal">
            <input type="text" className="form__input" placeholder="City" onChange={handleNameChange} list="city-datalist" />
            <button className="form__button" onClick={handleSubmit}> Search </button>

            <datalist id="city-datalist">
                {cityOptions.map(option => <option value={option.title} key={option.id} />)}
            </datalist>

            {error? <strong> {error} </strong> : null}
        </form>
    )
}