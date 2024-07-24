# This function calculates the windchill and returns it
def calculate_windchill(temperature, windspeed):
    windchill = 35.74 + 0.6215 * temperature - 35.75 * windspeed ** 0.16 + 0.4275 * temperature * (windspeed ** 0.16)
    return windchill
# This function converts the celsius temperature to fahrenheit
def convert_to_fahrenheit(temperature):
    new_temperature = (temperature * 9/5) + 32
    return new_temperature
# This function calculates the windchill when given celsius
def calculate_celsius_windchill(new_temperature, windspeed):
    windchill = 35.74 + 0.6215 * new_temperature - 35.75 * windspeed ** 0.16 + 0.4275 * new_temperature * (windspeed ** 0.16)
    return windchill

temperature = float(input("What is the temperature? "))
type = input("What is the type (C/F)? ")

windspeed = 0

while windspeed <= 55:
    windspeed += 5
    if type.upper() == "F":
        calculation = calculate_windchill(temperature, windspeed)
        print(f"At temperature {temperature}F, and wind speed {windspeed}, the windchill is: {calculation:.2f}F")
    if type.upper() == "C":
        new_temperature = convert_to_fahrenheit(temperature)
        celsius_calculation = calculate_celsius_windchill(new_temperature, windspeed)
        print(f"At temperature {new_temperature}F, and wind speed {windspeed}, the windchill is: {celsius_calculation:.2f}F")

