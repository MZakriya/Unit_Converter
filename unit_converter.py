import streamlit as st

# Distance Converter Function
def distance_converter(from_unit, to_unit, value):
    units = {
        "Meters": 1,
        "Kilometers": 1000,
        "Feet": 0.3048,
        "Miles": 1609.34,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

# Temperature Converter Function
def temperature_converter(from_unit, to_unit, value):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        result = (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        result = (value - 32) * 5/9
    else:
        result = value
    return result

# Weight Converter Function
def weight_converter(from_unit, to_unit, value):
    units = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

# Pressure Converter Function
def pressure_converter(from_unit, to_unit, value):
    units = {
        "Pascals": 1,
        "Hectopascals": 100,
        "Kilopascals": 1000,
        "Bar": 100000,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

# Streamlit UI
st.title("Unit Converter")

category = st.selectbox("Select Category", ["Distance", "Temperature", "Weight", "Pressure"])

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