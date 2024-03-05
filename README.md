# Weather Forecast App

This is a small Python application built using FastAPI to fetch temperature and rain forecasts for Lisbon in 3 days.

## Installation

1. Clone this repository.
2. Install dependencies using `pip3 install -r requirements.txt`.

## Usage

1. Sign up for an API key from OpenWeatherMap (https://home.openweathermap.org/users/sign_up) and replace `OPENWEATHERMAP_API_KEY` in `main.py` with your API key. I've left mine as an example.
2. Run the application using `uvicorn main:app --reload`.
3. Access the endpoints:
   - `/temperature`: Get the temperature forecast for Lisbon in 3 days.
   - `/rain`: Check if it will rain in Lisbon in 3 days.

## Testing

1. Run tests using `python3 test_main.py`.