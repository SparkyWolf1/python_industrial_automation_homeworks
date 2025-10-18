
# imports
import pathlib


# path to csv file with list of cities
CITY_LIST_CSV: pathlib.Path = (
    pathlib.Path.cwd()
    / 'DatasetsTesting'
    / 'Others'
    / 'seznam_mest.csv'
)

CITY_LOCATIONS_URL: str = "https://geocoding-api.open-meteo.com/v1/search"
CURRENT_WEATHER_URL: str = "https://api.open-meteo.com/v1/forecast?"

TESTING_CITIES = ["Praha", "Plzeň", "Jihlava"]
DEFAULT_SEARCH = 'Statutární město'
