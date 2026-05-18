#Importations

#for accesing system specific functions and parameters
import sys
#for helping in http requests and calling the api
import requests
#for json data handling
import json
#used for formartting the unique timestamsps
from datetime import datetime

API_KEY = "cb5ec66027fe4511a06160739261805" 
BASE_URL = "http://api.weatherapi.com/v1/current.json"



#function for taking city name as input and giving info details

def get_weather(city_name):
    "Fetches weather data"
    params = {
        'q':'city_name',
        'appid':API_KEY,
        #sets temperature to celsius instread of kelvin
        'units':'metric'
    }

    try:
        #makes http get request with base url
        response = requests.get(BASE_URL,params=params)
        #checks the http sucess codes
        response.raise_for_status()
        #returns the json response
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            print("❌ Error: Invalid API Key. Please check your configuration.")
        elif response.status_code == 404:
            print(f"❌ Error: City '{city_name}' not found.")
        else:
            print(f"❌ HTTP Error occurred: {http_err}")
        return None
    except requests.exceptions.ConnectionError:
        print("❌ Error: Failed to connect to the weather service. Check your internet.")
        return None
    except requests.exceptions.Timeout:
        print("❌ Error: The request timed out.")
        return None
    except requests.exceptions.RequestException as err:
        print(f"❌ An error occurred: {err}")
        return None

#function for displaying the data

def display_weather(data):
    if not data:
        return

    city = data['name']
    country = data['sys']['country']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description'].capitalize()
    wind_speed = data['wind']['speed']
    icon = data['weather'][0]['icon']

    print("\n" + "="*40)
    print(f"  🌤️  Weather Report for {city}, {country}")
    print("="*40)
    print(f"  Condition : {description}")
    print(f"  Temperature: {temp:.1f}°C")
    print(f"  Feels Like : {feels_like:.1f}°C")
    print(f"  Humidity   : {humidity}%")
    print(f"  Wind Speed : {wind_speed} m/s")
    print(f"  Last Update: {datetime.fromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*40 + "\n")

#function checking the program workflow

def main():
    if len(sys.args) < 2:
        print("Usage: python weather_cli.py <city_name>")
        print("Example: python weather_cli.py London")
        #if no argumet found exits with error
        sys.exit(1)

        city = " ".join(sys.argv[1:])
    print(f"🔍 Fetching weather for '{city}'...")
    
    weather_data = get_weather(city)
    if weather_data:
        display_weather(weather_data)


#standard python ididom to check the script is run directly if true it calls the main function
if __name__ == "__main__":
    main()
