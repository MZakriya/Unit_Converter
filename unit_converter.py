import streamlit as st

# Define all converter functions at the top
def distance_converter(from_unit, to_unit, value):
    units = {
        "Meters": 1,
        "Kilometers": 1000,
        "Feet": 0.3048,
        "Miles": 1609.34,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def temperature_converter(from_unit, to_unit, value):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        result = (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        result = (value - 32) * 5/9
    else:
        result = value
    return result

def weight_converter(from_unit, to_unit, value):
    units = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def pressure_converter(from_unit, to_unit, value):
    units = {
        "Pascals": 1,
        "Hectopascals": 100,
        "Kilopascals": 1000,
        "Bar": 100000,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def area_converter(from_unit, to_unit, value):
    units = {
        "Square Meters": 1,
        "Square Kilometers": 1e6,
        "Square Feet": 0.092903,
        "Square Miles": 2.59e6,
        "Acres": 4046.86,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def length_converter(from_unit, to_unit, value):
    units = {
        "Meters": 1,
        "Kilometers": 1000,
        "Feet": 0.3048,
        "Miles": 1609.34,
        "Inches": 0.0254,
        "Centimeters": 0.01,
        "Millimeters": 0.001,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def data_transfer_rate_converter(from_unit, to_unit, value):
    units = {
        "Bits per second": 1,
        "Kilobits per second": 1e3,
        "Megabits per second": 1e6,
        "Gigabits per second": 1e9,
        "Bytes per second": 8,
        "Kilobytes per second": 8e3,
        "Megabytes per second": 8e6,
        "Gigabytes per second": 8e9,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def digital_storage_converter(from_unit, to_unit, value):
    units = {
        "Bits": 1,
        "Bytes": 8,
        "Kilobytes": 8e3,
        "Megabytes": 8e6,
        "Gigabytes": 8e9,
        "Terabytes": 8e12,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def energy_converter(from_unit, to_unit, value):
    units = {
        "Joules": 1,
        "Kilojoules": 1e3,
        "Calories": 4.184,
        "Kilocalories": 4184,
        "Kilowatt-hours": 3.6e6,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def frequency_converter(from_unit, to_unit, value):
    units = {
        "Hertz": 1,
        "Kilohertz": 1e3,
        "Megahertz": 1e6,
        "Gigahertz": 1e9,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def fuel_economy_converter(from_unit, to_unit, value):
    units = {
        "Miles per gallon": 1,
        "Kilometers per liter": 2.35215,
        "Liters per 100 kilometers": 235.215,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def mass_converter(from_unit, to_unit, value):
    units = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495,
        "Metric Tons": 1000,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def plane_angle_converter(from_unit, to_unit, value):
    units = {
        "Degrees": 1,
        "Radians": 57.2958,
        "Gradians": 0.9,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def time_converter(from_unit, to_unit, value):
    units = {
        "Seconds": 1,
        "Minutes": 60,
        "Hours": 3600,
        "Days": 86400,
        "Weeks": 604800,
        "Years": 3.154e7,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def speed_converter(from_unit, to_unit, value):
    units = {
        "Meters per second": 1,
        "Kilometers per hour": 0.277778,
        "Miles per hour": 0.44704,
        "Feet per second": 0.3048,
        "Knots": 0.514444,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def volume_converter(from_unit, to_unit, value):
    units = {
        "Liters": 1,
        "Milliliters": 0.001,
        "Cubic Meters": 1000,
        "Cubic Feet": 28.3168,
        "Gallons": 3.78541,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

# Streamlit UI starts here
st.title("Unit Converter")

category = st.selectbox("Select Category", ["Distance", "Temperature", "Weight", "Pressure", "Area", "Length", "Data Transfer Rate", "Digital Storage", "Energy", "Frequency", "Fuel Economy", "Mass", "Plane Angle", "Time", "Speed", "Volume"])

if category == "Distance":
    from_unit = st.selectbox("From", ["Meters", "Kilometers", "Feet", "Miles"])
    to_unit = st.selectbox("To", ["Meters", "Kilometers", "Feet", "Miles"])
    value = st.number_input("Enter Value")
    result = distance_converter(from_unit, to_unit, value)
    st.write(f"<p style='font-size:24px;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)

elif category == "Temperature":
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit"])
    value = st.number_input("Enter Value")
    result = temperature_converter(from_unit, to_unit, value)
    st.write(f"<p style='font-size:24px;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)

elif category == "Weight":
    from_unit = st.selectbox("From", ["Kilograms", "Grams", "Pounds", "Ounces"])
    to_unit = st.selectbox("To", ["Kilograms", "Grams", "Pounds", "Ounces"])
    value = st.number_input("Enter Value")
    result = weight_converter(from_unit, to_unit, value)
    st.write(f"<p style='font-size:24px;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)

elif category == "Pressure":
    from_unit = st.selectbox("From", ["Pascals", "Hectopascals", "Kilopascals", "Bar"])
    to_unit = st.selectbox("To", ["Pascals", "Hectopascals", "Kilopascals", "Bar"])
    value = st.number_input("Enter Value")
    result = pressure_converter(from_unit, to_unit, value)
    st.write(f"<p style='font-size:24px;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)

elif category == "Area":
    from_unit = st.selectbox("From", ["Square Meters", "Square Kilometers", "Square Feet", "Square Miles", "Acres"])
    to_unit = st.selectbox("To", ["Square Meters", "Square Kilometers", "Square Feet", "Square Miles", "Acres"])
    value = st.number_input("Enter Value")
    result = area_converter(from_unit, to_unit, value)
    st.write(f"<p style='font-size:24px;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)

elif category == "Length":
    from_unit = st.selectbox("From", ["Meters", "Kilometers", "Feet", "Miles", "Inches", "Centimeters", "Millimeters"])
    to_unit = st.selectbox("To", ["Meters", "Kilometers", "Feet", "Miles", "Inches", "Centimeters", "Millimeters"])
    value = st.number_input("Enter Value")
    result = length_converter(from_unit, to_unit, value)
    st.write(f"<p style='font-size:24px;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)

elif category == "Data Transfer Rate":
    from_unit = st.selectbox("From", ["Bits per second", "Kilobits per second", "Megabits per second", "Gigabits per second", "Bytes per second", "Kilobytes per second", "Megabytes per second", "Gigabytes per second"])
    to_unit = st.selectbox("To", ["Bits per second", "Kilobits per second", "Megabits per second", "Gigabits per second", "Bytes per second", "Kilobytes per second", "Megabytes per second", "Gigabytes per second"])
    value = st.number_input("Enter Value")
    result = data_transfer_rate_converter(from_unit, to_unit, value)
    st.write(f"<p style='font-size:24px;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)

elif category == "Digital Storage":
    from_unit = st.selectbox("From", ["Bits", "Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes"])
    to_unit = st.selectbox("To", ["Bits", "Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes"])
    value = st.number_input("Enter Value")
    result = digital_storage_converter(from_unit, to_unit, value)
    st.write(f"<p style='font-size:24px;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)

elif category == "Energy":
    from_unit = st.selectbox("From", ["Joules", "Kilojoules", "Calories", "Kilocalories", "Kilowatt-hours"])
    to_unit = st.selectbox("To", ["Joules", "Kilojoules", "Calories", "Kilocalories", "Kilowatt-hours"])
    value = st.number_input("Enter Value")
    result = energy_converter(from_unit, to_unit, value)
    st.write(f"<p style='font-size:24px;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)

elif category == "Frequency":
    from_unit = st.selectbox("From", ["Hertz", "Kilohertz", "Megahertz", "Gigahertz"])
    to_unit = st.selectbox("To", ["Hertz", "Kilohertz", "Megahertz", "Gigahertz"])
    value = st.number_input("Enter Value")
    result = frequency_converter(from_unit, to_unit, value)
    st.write(f"<p style='font-size:24px;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)

elif category == "Fuel Economy":
    from_unit = st.selectbox("From", ["Miles per gallon", "Kilometers per liter", "Liters per 100 kilometers"])
    to_unit = st.selectbox("To", ["Miles per gallon", "Kilometers per liter", "Liters per 100 kilometers"])
    value = st.number_input("Enter Value")
    result = fuel_economy_converter(from_unit, to_unit, value)
    st.write(f"<p style='font-size:24px;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)

elif category == "Mass":
    from_unit = st.selectbox("From", ["Kilograms", "Grams", "Pounds", "Ounces", "Metric Tons"])
    to_unit = st.selectbox("To", ["Kilograms", "Grams", "Pounds", "Ounces", "Metric Tons"])
    value = st.number_input("Enter Value")
    result = mass_converter(from_unit, to_unit, value)
    st.write(f"<p style='font-size:24px;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)

elif category == "Plane Angle":
    from_unit = st.selectbox("From", ["Degrees", "Radians", "Gradians"])
    to_unit = st.selectbox("To", ["Degrees", "Radians", "Gradians"])
    value = st.number_input("Enter Value")
    result = plane_angle_converter(from_unit, to_unit, value)
    st.write(f"<p style='font-size:24px;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)

elif category == "Time":
    from_unit = st.selectbox("From", ["Seconds", "Minutes", "Hours", "Days", "Weeks", "Years"])
    to_unit = st.selectbox("To", ["Seconds", "Minutes", "Hours", "Days", "Weeks", "Years"])
    value = st.number_input("Enter Value")
    result = time_converter(from_unit, to_unit, value)
    st.write(f"<p style='font-size:24px;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)

elif category == "Speed":
    from_unit = st.selectbox("From", ["Meters per second", "Kilometers per hour", "Miles per hour", "Feet per second", "Knots"])
    to_unit = st.selectbox("To", ["Meters per second", "Kilometers per hour", "Miles per hour", "Feet per second", "Knots"])
    value = st.number_input("Enter Value")
    result = speed_converter(from_unit, to_unit, value)
    st.write(f"<p style='font-size:24px;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)

elif category == "Volume":
    from_unit = st.selectbox("From", ["Liters", "Milliliters", "Cubic Meters", "Cubic Feet", "Gallons"])
    to_unit = st.selectbox("To", ["Liters", "Milliliters", "Cubic Meters", "Cubic Feet", "Gallons"])
    value = st.number_input("Enter Value")
    result = volume_converter(from_unit, to_unit, value)
    st.write(f"<p style='font-size:24px;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)