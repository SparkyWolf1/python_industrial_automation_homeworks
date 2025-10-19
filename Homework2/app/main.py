
# -*- coding: utf-8 -*-
"""
Main program for Homework 2 - Communication with web APIs and Dashboards
Author: Ondřej Vitha
Date: 2025-10-15

Description:
This script sets up a Dash dashboard application that reads a list of cities
from a CSV file, processes the data, and initializes the dashboard with various
interactive components.
"""

# import standard libraries


# import third party libraries
import dash
import pandas

# import custom libraries
from data import constants
from data import shared_data
from models import current_weather
import data.request
import data.functions
import core.logger
import core.config
import components.layout


# define main program
def main() -> None:
    # setup logging
    core.logger.setup_logging(core.config.config_folder_name)

    # check for city names list csv file existence and raise error if not found
    if not constants.CITY_LIST_CSV.exists():
        core.logger.logger.error(
            f"File not found: {constants.CITY_LIST_CSV.resolve()}"
            )
        raise FileNotFoundError(
            f"File not found: {constants.CITY_LIST_CSV.resolve()}"
            )

    # read csv file with cities
    city_list: list[dict] = pandas.read_csv(
        constants.CITY_LIST_CSV,
        sep=';').to_dict(orient='records')

    # extract some information from city list
    # create sets for regions and districts
    # create dict for cities with status "Město", "Hlavní město"
    # or "Statutární město"
    # TODO: Refactor to posibly use dataclasses
    # TODO: make separte module and functions for data processing
    for city in city_list:
        shared_data.regions.add(city['Název Kraje (VÚSC)'])
        shared_data.districts.add(city['Název Okresu'])
        if (
            city['Status obce'] == 'Město' or
            city['Status obce'] == 'Hlavní město' or
            city['Status obce'] == 'Statutární město'
        ):
            shared_data.cities.append(city)
        # !Do NOT uncomment this call -> bug with endless loop...
        # shared_data.cities = data.functions.filter_data(
        #     data=city_list,
        #     keys=['Město','Hlavní město','Statutární město'],
        #     search_col='Status obce'
        # )

    # print(shared_data.cities)
    # log some information about city list
    core.logger.logger.info(
        f"City list read from {constants.CITY_LIST_CSV.resolve()}, "
        f"found {len(shared_data.cities)} cities, "
        f"{len(shared_data.districts)} districts and "
        f"{len(shared_data.regions)} regions."
    )

    # check if some cities, districts or regions were found
    if len(shared_data.cities) == 0:
        core.logger.logger.error("No cities found in city list.")
        raise ValueError("No cities found in city list.")

    if len(shared_data.districts) == 0:
        core.logger.logger.error("No districts found in city list.")
        raise ValueError("No districts found in city list.")

    if len(shared_data.regions) == 0:
        core.logger.logger.error("No regions found in city list.")
        raise ValueError("No regions found in city list.")

    # drop full city list not neded anymore
    del city_list

    # Create dashboard application
    Application: dash.Dash = dash.Dash(__name__)
    Application.title = "Weather Dasboard"

    for searched_item in shared_data.cities:
        if searched_item['Status obce'] == constants.DEFAULT_SEARCH:
            shared_data.searched_cities.append(searched_item['Název Obce'])

    positions = data.request.get_city_position(
        url=constants.CITY_LOCATIONS_URL,
        cities_name=shared_data.searched_cities,
        return_posibilities=1
    )
    temperatures: list[dict] = list()
    for item in positions:
        temperatures.append(
            data.request.get_current_weather(
                url=constants.CURRENT_WEATHER_URL,
                latitude=item["results"][0]["latitude"],
                longitude=item["results"][0]["longitude"]
                )
            )
    # print(temperatures[0]['current'])

    # Use the positions variable, for example, log its value
    core.logger.logger.info(f"City positions: {len(positions)}")

    for item_pos, item_weather in zip(positions, temperatures):
        # print(item["results"][0]["name"])
        current_data = current_weather.CurrentWeather(
            name=item_pos["results"][0]["name"],
            longtitude=item_pos["results"][0]["longitude"],
            latitude=item_pos["results"][0]["latitude"],
            temperature=item_weather["current"]["temperature_2m"],
            humidity=item_weather["current"]["relative_humidity_2m"],
            wind_speed=item_weather["current"]["wind_speed_10m"],
            description=""
            )
        shared_data.graphing_data.append(current_data.to_dict())

    core.logger.logger.info(shared_data.graphing_data)

    Application.layout = components.layout.create_layout(
        App=Application,
        data={}
    )
    Application.run(debug=True)


# run main program
if __name__ == '__main__':
    main()
