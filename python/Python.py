import requests

def get_weather(city):
    api_key = "your_api_key_here"
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": city
    }

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        location = data["location"]["name"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"The weather in {location} is {condition} with {temp_c}°C.")
    else:
        print("Failed to retrieve weather data.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
  
