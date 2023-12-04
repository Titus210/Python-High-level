async function fetchTemperatureAndHumidityData(latitude, longitude) {
    const apiUrl = `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m,relativehumidity_2m&forecast_days=1`;

    try {
        const response = await fetch(apiUrl);
        if (response.ok) {
            const data = await response.json();
            const hourlyData = data.hourly[0];
            if (hourlyData) {
                const temperature = hourlyData.temperature_2m[0];
                const humidity = hourlyData.relativehumidity_2m[0];

                return {
                    temperature: temperature,
                    humidity: humidity
                };
            } else {
                console.error("No temperature and humidity data found in the response.");
                return null;
            }
        } else {
            console.error(`Failed to fetch weather data. Status Code: ${response.status}`);
            return null;
        }
    } catch (error) {
        console.error("An error occurred:", error);
        return null;
    }
}

// Usage example with provided latitude and longitude
const latitude = 52.52; //  latitude
const longitude = 13.41; //  longitude

fetchTemperatureAndHumidityData(latitude, longitude)
    .then(weatherData => {
        if (weatherData) {
            console.log("Weather Data:");
            console.log(`Temperature: ${weatherData.temperature}°C`);
            console.log(`Humidity: ${weatherData.humidity}%`);
        }
    });
