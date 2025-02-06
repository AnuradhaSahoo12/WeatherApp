from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Replace with your OpenWeatherMap API Key
API_KEY = "800c6544079a1ba3eed32e59c4fbba4a"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def weather():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            params = {"q": city, "appid": "800c6544079a1ba3eed32e59c4fbba4a", "units": "metric"}
            response = requests.get(BASE_URL, params=params)

            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    "city": data["name"],
                    "temperature": f"{data['main']['temp']}°C",
                    "humidity": f"{data['main']['humidity']}%",
                    "wind_speed": f"{data['wind']['speed']} m/s",
                    "condition": data["weather"][0]["description"].title()
                }
            else:
                error = "City not found. Please enter a valid city name."

    return render_template("index.html", weather=weather_data, error=error)

if __name__ == "__main__":
    app.run(debug=True)
