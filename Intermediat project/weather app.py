import requests

# API details
API_KEY = "7fa2a4ce5e94f9651d241861609259fa"
BASE_URL ="http://api.openweathermap.org/data/2.5/weather"

# http://api.openweathermap.org/data/2.5/weather?q=london&appid=7fa2a4ce5e94f9651d241861609259fa&units=metric
# function to get weather data
def get_weather(city):
    try:
        # construct request url
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                "City": data["name"],
                "Temperature": data['main']["temp"],
                "Weather": data['weather'][0]['description'],
                "Humidity": data['main']['humidity'],
                
            }
            return weather
        elif response.status_code == 404:
            return "City not found, please check the name and try agian."
        else:
            return "Error Fetching data. please try again later."
    except requests.exceptions.RequestException as e:
        return f"An error Occurred: {e}"

# main program
def main():
    print("weather app")
    while True:
        city = input("\nEnter city name (or type'exit' to quit): ")
        if city.lower() == 'exit':
            break
        result = get_weather(city)
        if isinstance(result, dict):
            print(f"\nWeather in {result['City']}: ")
            print(f"\nTemprature: {result['Temperature']}°C")
            print(f"\nWeather: {result['Weather']}")
            print(f"\nHumidity: {result['Humidity']}%")
        else:
            print(result)

if __name__ =="__main__":
    main()