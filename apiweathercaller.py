import requests
import json

# Replace <YOUR_API_KEY> with your actual API key
api_key = "cc3a43505e8b44f389c11526242101"

# Example 1: Get current weather for London
url_current_weather = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=Encinitas"

# Example 2: Get 7-day weather forecast for US Zipcode 07112
#url_7_day_forecast = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q=07112&days=7"

# Example 3: Search for cities starting with Lond
#url_city_search = f"http://api.weatherapi.com/v1/search.json?key={api_key}&q=encini"

# Make requests
response_current_weather = requests.get(url_current_weather)
#response_7_day_forecast = requests.get(url_7_day_forecast)
#response_city_search = requests.get(url_city_search)



def write_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)


# Process responses
if response_current_weather.status_code == 200:
    data_current_weather = response_current_weather.json()
    write_to_json(data_current_weather, 'current_weather.json')
    # Process data for current weather as needed
    print("Current Weather Data:", data_current_weather)
else:
    print(f"Error in Current Weather Request: {response_current_weather.status_code}")


