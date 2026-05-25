# Weather App

A lightweight, production-ready weather application built using only two core files:

* `index.html`
* `api.js`

The project fetches real-time weather data from a weather API and displays current conditions with a clean UI and fast response time.

---

## Features

* Real-time weather data
* City-based weather search
* Temperature, humidity, wind speed, and condition display
* Responsive UI for desktop and mobile
* Minimal project structure
* API separation for maintainability
* Fast loading and lightweight architecture

---

## Tech Stack

| Technology        | Purpose                |
| ----------------- | ---------------------- |
| HTML5             | Structure              |
| CSS3              | Styling                |
| JavaScript (ES6+) | Logic and API handling |
| Weather API       | Live weather data      |

---

# Project Structure

```bash
weather-app/
│
├── index.html      # Main UI and frontend logic
├── api.js          # API requests and weather handling
└── README.md
```

---

# Workflow

## 1. User Interaction

The user enters a city name in the search field.

```text
User Input → Search Button Click
```

---

## 2. Request Handling

`index.html` captures the input and calls functions from `api.js`.

```text
index.html → api.js
```

---

## 3. API Fetch

`api.js` sends a request to the weather API.

```text
api.js → Weather API
```

Example flow:

```js
fetch(`API_URL?q=${city}&appid=${API_KEY}`)
```

---

## 4. Response Processing

The API returns JSON weather data.

```text
Weather API → JSON Response
```

`api.js` extracts:

* Temperature
* Weather condition
* Humidity
* Wind speed
* Location details

---

## 5. UI Rendering

Processed data is sent back to `index.html` and displayed dynamically.

```text
api.js → index.html → Browser UI
```

---

# Architecture Overview

```text
┌──────────────┐
│   User UI    │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ index.html   │
│ UI Handling  │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   api.js     │
│ API Requests │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Weather API  │
└──────────────┘
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/VasuML07/weather-app.git
```

---

## 2. Open Project

```bash
cd weather-app
```

---

## 3. Configure API Key

Inside `api.js`, replace the placeholder API key:

```js
const API_KEY = "YOUR_API_KEY";
```

You can get an API key from:

* OpenWeatherMap
* WeatherAPI
* Tomorrow.io

---

## 4. Run Project

Open `index.html` directly in the browser.

Or run with VS Code Live Server.

---

# Example API Response

```json
{
  "name": "Hyderabad",
  "main": {
    "temp": 31,
    "humidity": 58
  },
  "wind": {
    "speed": 4.2
  },
  "weather": [
    {
      "main": "Clouds"
    }
  ]
}
```

---

# Performance Considerations

* Minimal file structure reduces overhead
* Separation of API logic improves maintainability
* Asynchronous fetch requests prevent UI blocking
* Lightweight frontend with no framework dependency

---

# Future Improvements

* 5-day weather forecast
* Geolocation support
* Dark mode
* Unit conversion (°C / °F)
* Error handling improvements
* Loading animations
* Weather icons and background effects

---

# Security Notes

Avoid exposing production API keys directly in frontend projects.

For production deployment:

* Use environment variables
* Add backend proxy handling
* Restrict API key usage by domain

---

# Deployment

This project can be deployed easily on:

* GitHub Pages
* Netlify
* Vercel
* Firebase Hosting

---

# License

This project is open-source and available under the MIT License.

---

# Author

Developed by VasuML07.

GitHub Repository:

[weather-app repository](https://github.com/VasuML07/weather-app?utm_source=chatgpt.com)
