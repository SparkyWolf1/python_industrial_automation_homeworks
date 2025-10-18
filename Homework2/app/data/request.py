import requests


def get_current_weather(
        url: str,
        timeout: int = 5,
        latitude: float = 50.08804,
        longitude: float = 14.42076,
        api_key: str | None = None
        ) -> requests.Response | None:
    request_url = (
        url
        + f'latitude={latitude}&'
        + f'longitude={longitude}'
        + '&current=temperature_2m,relative_humidity_2m,wind_speed_10m'

    )
    try:
        headers = {"Accept": "application/json",
                   "Accept-Encoding": "deflate, gzip, br"}
        if api_key is not None:
            headers["Authorization"] = f"Bearer {api_key}"
        response = requests.get(request_url,
                                timeout=timeout,
                                headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as Err:
        raise SystemExit(Err) from Err


def get_city_position(
        url: str,
        cities_name: list[str],
        return_posibilities: int,
        timeout: int = 5
) -> list[dict]:
    headers = {"Accept": "application/json",
               "Accept-Encoding": "deflate, gzip, br"}

    cities_positions: list[dict] = list()
    for city in cities_name:
        request_url = (
            url
            + f"?name={city}"
            + f"&count={return_posibilities}"
            + "&language=en"
            + "&format=json"
            )
        response = requests.get(
            url=request_url,
            timeout=timeout,
            headers=headers
        )
        if response.status_code == 200:
            cities_positions.append(response.json())
    return cities_positions
