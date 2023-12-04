import requests

def fetchTemperatureAndHumidityData(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relativehumidity_2m&forecast_days=16"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            hourly_data = data.get("hourly", [])
            if hourly_data:
                time = hourly_data.get("time", [])
                temperature = hourly_data.get("temperature_2m", [])
                humidity = hourly_data.get("relativehumidity_2m", [])
                
                structured_data = {
                    "time": time,
                    "temperature": temperature,
                    "humidity": humidity
                }
                
                return structured_data
            else:
                print("No hourly data found in the response.")
                return None
        else:
            print(f"Failed to fetch weather data. Status Code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Usage example with provided latitude and longitude
latitude = 52.52  # Replace with your latitude
longitude = 13.41  # Replace with your longitude

weather_data = fetchTemperatureAndHumidityData(latitude, longitude)
if weather_data:
    print("Weather Data:")
    for i in range(len(weather_data["time"])):
        print(f"Time: {weather_data['time'][i]}, Temperature: {weather_data['temperature'][i]}°C, Humidity: {weather_data['humidity'][i]}%")
