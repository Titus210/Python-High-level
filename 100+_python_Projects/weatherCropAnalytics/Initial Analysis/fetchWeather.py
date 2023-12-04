import requests

def fetchTemperatureAndHumidityData(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relativehumidity_2m&forecast_days=1"
    
    try:
        response = requests.get(url)
        print(response)
        data = response.json()
        
        if response.status_code == 200:
            hourly_data = data.get("hourly", [])
            
            # only fetch data when hourly status has been fetched
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

# latitude and longitude 
latitude = 52.52  
longitude = 13.41  


weather_data = fetchTemperatureAndHumidityData(latitude, longitude)
if weather_data:
    print("Weather Data:")
    print(f"Temperature: {weather_data['temperature']}°C")
    print(f"Humidity: {weather_data['humidity']}%")
