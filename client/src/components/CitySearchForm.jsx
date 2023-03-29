import { useEffect, useState } from "react"
import { useNavigate } from "react-router-dom"

export default function CitySearchForm() {
    const [cityName, setCityName] = useState()
    const [cityOptions, setCityOptions] = useState([])
    const [error, setError] = useState()

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
    // eslint-disable-next-line
    }, [cityName])

    const handleSubmit = async e => {
        e.preventDefault()
        setError(false)

        let response = await fetch(`http://127.0.0.1:8000/api/forecast/get-city-id/${cityName}`)

        if (!response.ok) {
            setError('City is not found')

            return
        }

        let json = await response.json()
        console.log(json.id)

        navigate(`/forecast/${json.id}`)
    }

    return (
        <form className="form header__form form_horizontal form_search">
            <input type="text" className="input form__input input_search" placeholder="City" onChange={handleNameChange} list="city-datalist" />
            <button className="button form__button button_search" onClick={handleSubmit}> Search </button>

            <datalist id="city-datalist">
                {cityOptions.map(option => <option value={option.title} key={option.id} />)}
            </datalist>

            {error? <strong className="form__error"> {error} </strong> : null}
        </form>
    )
}