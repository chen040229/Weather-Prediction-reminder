
import requests
import os

api_key = "please fill your api key"
base_url = "http://api.weatherapi.com/v1/"

# paths
forecast = "forecast.json"
current = "current.json"

class Weather:

    def __init__(self, api_key: str, base_url: str) -> None:
        self.api_key = api_key
        self.base_url = base_url

    def get_ith_day_weather(self, i: int) -> dict:
        path = "forecast.json"
        target_url = os.path.join(base_url, path)

        params = {
            "key": api_key,
            "q": "your city",
            "days": i
        }

        # 4. create the request
        resp = requests.get(target_url, params=params, headers={"Accept": "application/json"})

        # 5. check the response
        status_code = resp.status_code
        if status_code != 200:
            # string interpolation
            print(f"Error: {status_code}, {resp.content}")

        content = resp.json()

        day_forecast = content["forecast"]["forecastday"][i-1]["day"]
        maxtemp = day_forecast["maxtemp_c"]
        mintemp = day_forecast["mintemp_c"]
        avetemp = day_forecast["avgtemp_c"]
        uv = day_forecast["uv"]
        will_it_rain = day_forecast["daily_will_it_rain"]
        chance_of_rain = day_forecast["daily_chance_of_rain"]

        res = {
            "Forcast":"FORECASTING",
            "City": "wuhan",
            "max_temp": maxtemp,
            "min_temp": mintemp,
            "ave_temp": avetemp,
            "uv": uv,
            "will_it_rain": will_it_rain,
            "chance_of_rain": chance_of_rain
        }

        return res

    # TODO
    def get_current_weather(self) -> dict:
        path = "current.json"
        target_url = os.path.join(base_url,path)

        params = {
            "key": api_key,
            "q": "Wuhan"
        }

        resp = requests.get(target_url, params=params, headers={"Accept": "application/json"})

        status_code = resp.status_code
        if status_code != 200:
            print(f"Error: {status_code}, {resp.content}")
        
        content = resp.json()
        current = content["current"]
        last_updated = current["last_updated"]
        last_updated_epoch = current["last_updated_epoch"]
        temp = current["temp_c"]
        condition = current["condition"]["text"]
        wind_kph = current["wind_kph"]
        humidity = current["humidity"]
        uv = current["uv"]
        cloud = current["cloud"]

        res = {
            "Current_Weater": "current_weather description",
            "City": "Your City",
            "last_updated" : last_updated,
            "last_updated_epoch" : last_updated_epoch,
            "temp": temp,
            "condition": condition,
            "wind_kph": wind_kph,
            "humidity": humidity,
            "uv": uv,
            "cloud":cloud

        }

        return res

    # TODO
    def get_ith_astro(self) -> dict:
        path = "astronomy.json"
        target_url = os.path.join(base_url, path)

        params = {
            "key": api_key,
            "q": "Your city",
            "dt": "Your date"
        }

        resp = requests.get(target_url, params=params, headers={"Accept": "application/json"})

        status_code = resp.status_code
        if status_code != 200:
            print(f"Error: {status_code}, {resp.content}")

        content = resp.json()
        astronomy = content["astronomy"]["astro"]
        sunrise = astronomy["sunrise"]
        sunset = astronomy["sunset"]
        moonrise = astronomy["moonrise"]
        moonset = astronomy["moonset"]
        moon_phase = astronomy["moon_phase"]
        mmoon_illumination = astronomy["moon_illumination"]

        res = {
            "Astro" : "Astronomy",
            "City": "Your City",
            "sunrise" : sunrise,
            "sunset" : sunset,
            "moonrise": moonrise,
            "moonset": moonset,
            "moon_phase": moon_phase,
            "mmoon_illumination": mmoon_illumination,

        }

     
        return res

if __name__ == "__main__":
    weather = Weather(api_key, base_url)
    print(weather.get_ith_day_weather(1))
