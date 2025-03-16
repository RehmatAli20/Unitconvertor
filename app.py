import streamlit as st

# Conversion functions
def convert_length(value, from_unit, to_unit):
    length_units = {
        "Meters": 1, "Kilometers": 1000, "Centimeters": 0.01, "Millimeters": 0.001,
        "Miles": 1609.34, "Yards": 0.9144, "Feet": 0.3048, "Inches": 0.0254, "Nautical Miles": 1852
    }
    return value * length_units[to_unit] / length_units[from_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    conversions = {
        "Celsius": lambda x: x,
        "Fahrenheit": lambda x: x * 9 / 5 + 32,
        "Kelvin": lambda x: x + 273.15
    }
    return conversions[to_unit](conversions[from_unit](value))

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1, "Grams": 0.001, "Milligrams": 1e-6, "Pounds": 0.453592,
        "Ounces": 0.0283495, "Tons (metric)": 1000, "Tons (US)": 907.1847, "Stones": 6.35029
    }
    return value * weight_units[to_unit] / weight_units[from_unit]

def convert_volume(value, from_unit, to_unit):
    volume_units = {
        "Liters": 1, "Milliliters": 0.001, "Cubic meters": 1000, "Cubic centimeters": 0.001,
        "Gallons (US)": 3.78541, "Gallons (UK)": 4.54609, "Pints (US)": 0.473176, "Pints (UK)": 0.568261
    }
    return value * volume_units[to_unit] / volume_units[from_unit]

def convert_speed(value, from_unit, to_unit):
    speed_units = {
        "Meters per second": 1, "Kilometers per hour": 3.6, "Miles per hour": 2.23694,
        "Knots": 1.94384, "Feet per second": 3.28084
    }
    return value * speed_units[to_unit] / speed_units[from_unit]

def convert_time(value, from_unit, to_unit):
    time_units = {
        "Seconds": 1, "Minutes": 60, "Hours": 3600, "Days": 86400, "Weeks": 604800,
        "Months": 2.628e6, "Years": 3.154e7
    }
    return value * time_units[to_unit] / time_units[from_unit]

def convert_energy(value, from_unit, to_unit):
    energy_units = {
        "Joules": 1, "Kilojoules": 1000, "Calories": 4.184, "Kilocalories": 4184,
        "Watt-hours": 3600, "Kilowatt-hours": 3.6e6, "Electronvolts": 1.60218e-19
    }
    return value * energy_units[to_unit] / energy_units[from_unit]

def convert_digital_storage(value, from_unit, to_unit):
    storage_units = {
        "Bytes": 1, "Kilobytes": 1024, "Megabytes": 1048576, "Gigabytes": 1073741824,
        "Terabytes": 1099511627776, "Petabytes": 1.12589991e15
    }
    return value * storage_units[to_unit] / storage_units[from_unit]

def convert_area(value, from_unit, to_unit):
    area_units = {
        "Square meters": 1, "Square kilometers": 1e6, "Square miles": 2.59e6,
        "Acres": 4046.86, "Hectares": 10000, "Square feet": 0.092903, "Square inches": 0.00064516
    }
    return value * area_units[to_unit] / area_units[from_unit]

def convert_fuel_efficiency(value, from_unit, to_unit):
    fuel_units = {
        "Kilometers per liter": 1, "Miles per gallon (US)": 2.35215, "Miles per gallon (UK)": 2.82481,
        "Liters per 100 km": 235.215
    }
    return value * fuel_units[to_unit] / fuel_units[from_unit]

def convert_pressure(value, from_unit, to_unit):
    pressure_units = {
        "Pascals": 1, "Bars": 1e5, "Atmospheres": 101325, "Pounds per square inch": 6894.76
    }
    return value * pressure_units[to_unit] / pressure_units[from_unit]

def convert_power(value, from_unit, to_unit):
    power_units = {
        "Watts": 1, "Kilowatts": 1000, "Horsepower (metric)": 735.5, "Horsepower (US)": 745.7,
        "BTU per hour": 0.293071
    }
    return value * power_units[to_unit] / power_units[from_unit]

# UI
st.title("Unit Converter")
st.subheader("Convert various units like Google’s converter")

categories = {
    "Length": convert_length, "Temperature": convert_temperature, "Weight": convert_weight,
    "Volume": convert_volume, "Speed": convert_speed, "Time": convert_time,
    "Energy": convert_energy, "Digital Storage": convert_digital_storage,
    "Area": convert_area, "Fuel Efficiency": convert_fuel_efficiency,
    "Pressure": convert_pressure, "Power": convert_power
}

category = st.selectbox("Select Category", list(categories.keys()))

units = {
    "Length": ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches", "Nautical Miles"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Weight": ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces", "Tons (metric)", "Tons (US)", "Stones"],
    "Volume": ["Liters", "Milliliters", "Cubic meters", "Cubic centimeters", "Gallons (US)", "Gallons (UK)", "Pints (US)", "Pints (UK)"],
    "Speed": ["Meters per second", "Kilometers per hour", "Miles per hour", "Knots", "Feet per second"],
    "Time": ["Seconds", "Minutes", "Hours", "Days", "Weeks", "Months", "Years"],
    "Energy": ["Joules", "Kilojoules", "Calories", "Kilocalories", "Watt-hours", "Kilowatt-hours", "Electronvolts"],
    "Digital Storage": ["Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes", "Petabytes"],
    "Area": ["Square meters", "Square kilometers", "Square miles", "Acres", "Hectares", "Square feet", "Square inches"],
    "Fuel Efficiency": ["Kilometers per liter", "Miles per gallon (US)", "Miles per gallon (UK)", "Liters per 100 km"],
    "Pressure": ["Pascals", "Bars", "Atmospheres", "Pounds per square inch"],
    "Power": ["Watts", "Kilowatts", "Horsepower (metric)", "Horsepower (US)", "BTU per hour"]
}

value = st.number_input("Enter value", value=1.0)
from_unit = st.selectbox("From unit", units[category])
to_unit = st.selectbox("To unit", units[category])

result = categories[category](value, from_unit, to_unit)
st.write(f"**{value} {from_unit} = {result} {to_unit}**")
