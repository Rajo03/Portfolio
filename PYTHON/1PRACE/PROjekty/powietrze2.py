import asyncio
import logging

from accuweather import (
    AccuWeather,
    ApiError,
    InvalidApiKeyError,
    InvalidCoordinatesError,
    RequestsExceededError,
)
from aiohttp import ClientError, ClientSession

LATITUDE = 50.6687353
LONGITUDE = 18.6846192
LOCATION_KEY = "265963"
API_KEY = "NA4S6hPV5VqShjhy4ISya6m5J5pijTDv"

logging.basicConfig(level=logging.DEBUG)


async def main():
    async with ClientSession() as websession:
        try:
            accuweather = AccuWeather(
                API_KEY, websession, latitude=LATITUDE, longitude=LONGITUDE
            )
            current_conditions = await accuweather.async_get_current_conditions()
            forecast = await accuweather.async_get_forecast(metric=True)
        except (
            ApiError,
            InvalidApiKeyError,
            InvalidCoordinatesError,
            ClientError,
            RequestsExceededError,
        ) as error:
            print(f"Error: {error}")
        else:
            print(f"Location: {accuweather.location_name} ({accuweather.location_key})")
            print(f"Requests remaining: {accuweather.requests_remaining}")
            print(f"Current: {current_conditions}")
            print(f"Forecast: {forecast}")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
