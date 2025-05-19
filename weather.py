Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import streamlit as st
import requests

# Emojis for different weather conditions
weather_icons = {
    "Clear": "☀️",
    "Clouds": "☁️",
    "Rain": "🌧️",
    "Drizzle": "🌦️",
    "Thunderstorm": "⛈️",
    "Snow": "❄️",
    "Mist": "🌫️",
    "Smoke": "💨",
    "Haze": "🌁",
    "Dust": "🌪️",
    "Fog": "🌫️",
    "Sand": "🏜️",
    "Ash": "🌋",
    "Squall": "💨",
    "Tornado": "🌪️"
}

# Counterattack-style error
def show_error():
    st.error("💥 Oops! Weather server dodged our request like a ninja. Try again or check the city name.")

... # Weather fetch function
... def get_weather(city):
...     try:
...         API_KEY = "4d8fb5b93d4af21d66a2948710284366"  # Replace with your real API key
...         URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
...         response = requests.get(URL)
...         if response.status_code == 200:
...             return response.json()
...         else:
...             return None
...     except:
...         return None
... 
... # UI
... st.set_page_config(page_title="Weather Wizard 🌦️", page_icon="🌦️")
... st.title("🧙‍♂️ Weather Forecasting Wizard")
... st.write("Enter a city name to summon the latest weather insights!")
... 
... city = st.text_input("📍 City Name", "Bangalore")
... 
... if st.button("🔍 Get Forecast"):
...     data = get_weather(city)
...     
...     if data:
...         main = data['weather'][0]['main']
...         desc = data['weather'][0]['description'].capitalize()
...         temp = data['main']['temp']
...         feels = data['main']['feels_like']
...         humidity = data['main']['humidity']
...         wind = data['wind']['speed']
...         icon = weather_icons.get(main, "🌈")
...         
...         st.markdown(f"### {icon} Weather in **{city.title()}**")
...         st.write(f"**Condition:** {desc}")
...         st.write(f"**Temperature:** {temp}°C (Feels like {feels}°C)")
...         st.write(f"**Humidity:** {humidity}%")
...         st.write(f"**Wind Speed:** {wind} m/s")
...     else:
...         show_error()
... 
... st.caption("🔁 Built with the same spirit as Emotion Detector 3.0 – resilient and playful!")
