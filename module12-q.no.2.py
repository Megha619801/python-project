#Q.no.2
import requests


def get_weather_for_city(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        weather_description = data['weather'][0]['description']
        temperature_kelvin = data['main']['temp']

        temperature_celsius = temperature_kelvin - 273.15

        print(f"Weather in {city_name.capitalize()}:")
        print(f"Condition: {weather_description.capitalize()}")
        print(f"Temperature: {temperature_celsius:.2f}°C")
    else:
        print("Failed to retrieve weather data. Please check the city name and try again.")


if __name__ == "__main__":
    city_name = input("Enter the name of the municipality: ")
    api_key = "YOUR_API_KEY"
    get_weather_for_city(city_name, api_key)