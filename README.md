# Windchill-Calculator

This Python script calculates the windchill based on temperature and wind speed input. It supports both Celsius and Fahrenheit temperature inputs.

## Features

- **Calculate Windchill**: Calculates the windchill using the formula:
windchill = 35.74 + 0.6215 * temperature - 35.75 * windspeed ** 0.16 + 0.4275 * temperature * (windspeed ** 0.16)

- **Convert Celsius to Fahrenheit**: Converts Celsius temperature to Fahrenheit using the formula:
fahrenheit = (celsius * 9/5) + 32

- **Interactive Input**: Asks the user for temperature and type (Celsius or Fahrenheit), then computes windchill for various wind speeds up to 60 mph.

## Usage

1. Clone the repository:
git clone <repository-url>

2. Navigate to the directory:
cd windchill-calculator

3. Run the script:
python windchill_calculator.py

4. Follow the prompts to enter temperature and type (C/F).

## Example

Sample interaction:
What is the temperature? 10
What is the type (C/F)? C

At temperature 50.0F, and wind speed 5, the windchill is: 3.50F
At temperature 50.0F, and wind speed 10, the windchill is: -0.40F
At temperature 50.0F, and wind speed 15, the windchill is: -3.30F

## Contributors

- [Carson Landvatter](https://github.com/carsonlandvatter)
