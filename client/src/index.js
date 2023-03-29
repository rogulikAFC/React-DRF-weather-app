import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
// import './reset-default-styles.css'
import App from './App';
import { BrowserRouter } from 'react-router-dom';

import './css/header.css'
import './css/form.css'
import './css/card.css'
import './css/weather-mini-card.css'

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
);
