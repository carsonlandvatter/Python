# Windchill-Calculator

This Python script calculates the windchill based on temperature and wind speed input. It supports both Celsius and Fahrenheit temperature inputs.

## Features

- **Calculate Windchill**: Calculates the windchill using the formula:
windchill = 35.74 + 0.6215 * temperature - 35.75 * windspeed ** 0.16 + 0.4275 * temperature * (windspeed ** 0.16)

- **Convert Celsius to Fahrenheit**: Converts Celsius temperature to Fahrenheit using the formula:
fahrenheit = (celsius * 9/5) + 32

- **Interactive Input**: Asks the user for temperature and type (Celsius or Fahrenheit), then computes windchill for various wind speeds up to 55 mph.
