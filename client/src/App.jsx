import './App.css';
import { Route, Routes } from 'react-router-dom'
import Root from './routes/Root';
import ForecastDay from './routes/DailyForecast';
import CitySearchForm from './components/CitySearchForm';

function App() {
    // const router = createBrowserRouter([
    //     {
    //         path: '/',
    //         element: <Root />
    //     },
    //     {
    //         path: '/forecast/:cityId/',
    //         element: <ForecastDay />
    //     }
    // ])

    return (
        <div className="App">
            <header className="header App__header">
                <h2 className="header__title"> WeatherApp </h2>
                <CitySearchForm />
            </header>

            <main className="main App__main">
                <Routes>
                    <Route path='/' element={<Root />}/>
                    <Route path='/forecast/:cityId/' element={<ForecastDay />}/>
                </Routes>
            </main>

            <footer className="App__footer">
                <div className="footer__info">
                    <a href=".">Terms and conditions</a>
                </div>
            </footer>
        </div>
  );
}

export default App;
