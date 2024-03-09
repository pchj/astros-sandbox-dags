from airflow import Dataset
from airflow.decorators import dag, task
from pendulum import datetime
import requests
import os

# Replace YOUR_API_KEY with your actual OpenWeatherMap API key
API_KEY = os.getenv("OPENWEATHER_API_KEY")
MADISON_LAT = 43.0731
MADISON_LON = -89.4012

@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    doc_md="""
    ## Weather Data ETL for Madison, Wisconsin

    This DAG retrieves the current weather data for Madison, Wisconsin from 
    the OpenWeatherMap API and prints the temperature and weather conditions.

    The process consists of two tasks: one to fetch the weather data and another 
    to print the results. Utilizing Airflow's TaskFlow API, these Python functions 
    become Airflow tasks with automatically inferred dependencies and data passing.

    For more explanation and getting started instructions with Airflow, 
    visit the Write your first DAG tutorial: 
    https://docs.astronomer.io/learn/get-started-with-airflow
    """,
    default_args={"owner": "Astro", "retries": 3},
    tags=["weather", "madison"],
)
def weather_data_madison():
    @task(outlets=[Dataset("madison_weather_data")])
    def get_weather_data(**context) -> dict:
        """
        Fetches the current weather data for Madison, Wisconsin, using the 
        OpenWeatherMap API. The result is returned and can be used in downstream tasks.
        """
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={MADISON_LAT}&lon={MADISON_LON}&appid={API_KEY}&units=imperial"
        response = requests.get(url)
        weather_data = response.json()
        return weather_data

    @task
    def print_weather_details(weather_data: dict) -> None:
        """
        Prints the temperature and weather condition for Madison, Wisconsin,
        based on the data retrieved from the OpenWeatherMap API.
        """
        temp = weather_data['main']['temp']
        condition = weather_data['weather'][0]['description']
        print(f"The current temperature in Madison is {temp}°F with {condition}.")

    print_weather_details(get_weather_data())

weather_data_madison()
