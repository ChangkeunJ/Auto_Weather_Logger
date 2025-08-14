
# Auto Weather Logger

This project automatically logs hourly temperature data for major cities in South Korea using GitHub Actions and the Open-Meteo API.

## Features

- **Hourly Logging**  
  A GitHub Actions workflow runs every hour to fetch live temperature data via Open-Meteo.

- **Supports Major Korean Cities**  
  Includes 17 key cities such as 서울, 부산, 인천, 대구, 대전, 광주, 울산, 수원, 제주, and more.

- **Accurate Location-Based Data**  
  Each city uses precise latitude and longitude coordinates to retrieve localized weather.

- **Temperature in Celsius**  
  All data is retrieved in metric units (°C) from the Open-Meteo API.

- **Korean Output**  
  Logs display city names in Korean (e.g., 서울, 부산), while using geo-coordinates for API requests.

- **Daily Log Files**  
  Temperature logs are stored in `logs/YYYY-MM-DD.txt` format, with one file generated per day.

## Example Log Entry

```
[2025-07-30 01:00:00]
서울: 27.3°C
부산: 25.1°C
인천: 26.2°C
...
```
...

## How It Works

- The GitHub Actions workflow is scheduled using cron to run at the top of every hour.
- A Python script calls the Open-Meteo API using latitude/longitude coordinates for each city.
- The hourly temperature data is parsed from the API's JSON response and logged to a dated text file.
- Changes are committed and pushed automatically to update GitHub contribution activity.

## Weather Data Source

Powered by the [Open-Meteo API](https://open-meteo.com/), a free weather forecast API providing global weather data based on geographic coordinates.
