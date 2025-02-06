# Project: WeatherApp using Flask
This project is a Weather Application built with Flask that fetches real-time weather data from the OpenWeatherMap API and displays it in a web browser. The application allows users to enter a city name and retrieve weather details such as temperature, humidity, wind speed, and weather conditions.


Features
✅ User Input for City Name
✅ Fetches Weather Data from OpenWeatherMap API
✅ Displays Temperature, Humidity, Wind Speed, and Weather Condition
✅ Flask Web Interface for a Simple UI
✅ Error Handling for Invalid City Names

**Project Structure**
weatherApp/
│── app.py                  # Main Flask application
│── templates/               # HTML templates folder
│    ├── index.html          # Frontend UI for weather display
│── static/                  # (Optional) For CSS & JavaScript files
│── README.md                # Project description & setup guide
│── requirements.txt         # Dependencies for the project


How It Works
1️⃣ The user enters a city name in the web app.
2️⃣ The app sends a request to the OpenWeatherMap API using requests.get().
3️⃣ The API returns temperature, humidity, wind speed, and weather condition.
4️⃣ The Flask app displays the data dynamically on index.html.
5️⃣ If an invalid city is entered, an error message is shown.

**Setup & Installation**
Get OpenWeatherMap API Key
Sign up at https://openweathermap.org/api
Get a free API Key
Replace "your_api_key_here" in app.py with your API key

**Run the Flask App**
Go to http://127.0.0.1:5000/ in your browser.
