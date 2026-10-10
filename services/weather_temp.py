import requests

def get_weather(latitude, longitude):

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m"
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        temperature = data.get("current", {}).get("temperature_2m")

        if temperature is None:
            raise ValueError("Temperature data not found")

        return float(temperature)

    except requests.exceptions.RequestException as e:
        raise ValueError(
            f"Weather API connection failed: {e}"
        ) from e

    except (ValueError, TypeError, KeyError) as e:
        raise ValueError(
            f"Invalid weather data: {e}"
        ) from e
