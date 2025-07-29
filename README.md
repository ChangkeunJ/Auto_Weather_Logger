## Auto Weather Logger — GitHub Actions Summary

This project automatically logs hourly temperature data for major cities in South Korea using GitHub Actions and the [wttr.in](https://wttr.in) API.

### Features

* **Hourly Logging**
  A GitHub Actions workflow runs every hour to fetch live temperature data.

* **Supports Major Korean Cities**
  Includes 17 key cities such as Seoul, Busan, Incheon, Daegu, Daejeon, Gwangju, Ulsan, Suwon, Jeju, and more.

* **Temperature in Celsius**
  All temperatures are retrieved in Celsius (°C) by specifying metric units in the API query.

* **Korean Output**
  Logs display city names in Korean (e.g., 서울, 부산) while using English identifiers internally for API requests.

* **Daily Log Files**
  Temperature logs are stored in `logs/YYYY-MM-DD.txt` format, with one file per day.

### Example Log Entry

```
[2025-07-30 01:00:00]
서울: +27°C
부산: +25°C
인천: +26°C
...
```

### How It Works

* The GitHub Actions workflow is scheduled using `cron` to run at the top of every hour.
* The Python script sends HTTP requests to `wttr.in` for each city and appends the results to the current day's log file.
* Changes are committed and pushed automatically to ensure contribution activity is updated.
