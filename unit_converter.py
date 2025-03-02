import streamlit as st
import requests

# Set page config for a better theme and layout
st.set_page_config(
    page_title="Unit Converter",
    page_icon="📏",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 10px 24px;
        font-size: 16px;
    }
    .stSelectbox div {
        font-size: 18px;
    }
    .stNumberInput input {
        font-size: 18px;
    }
    h1 {
        color: #4CAF50;
        text-align: center;
    }
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

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

# Currency Converter Function
def currency_converter(from_currency, to_currency, value):
    API_KEY = "00a7a69960b0817d262bae67"  # Replace with your API key
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes (4xx or 5xx)
        data = response.json()

        if response.status_code == 200:
            if "conversion_rates" in data:
                exchange_rate = data["conversion_rates"][to_currency]
                result = value * exchange_rate
                return result
            else:
                st.error("Invalid API response. Please check your API key or try again later.")
                return None
        else:
            st.error(f"API Error: {data.get('error', 'Unknown error')}")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to connect to the API: {e}")
        return None
    except ValueError as e:
        st.error(f"Invalid JSON response: {e}")
        return None

# Sidebar for additional options or info
with st.sidebar:
    st.header("📝 About")
    st.markdown("""
        **Welcome to the Unit Converter App!** 🎉

        This app allows you to convert between various units across multiple categories, including:
        - **Distance**: Meters, Kilometers, Feet, Miles
        - **Temperature**: Celsius, Fahrenheit
        - **Weight**: Kilograms, Grams, Pounds, Ounces
        - **Currency**: USD, EUR, GBP, PKR, and more!
        - And many more categories like Area, Length, Data Transfer Rate, Digital Storage, Energy, Frequency, Fuel Economy, Mass, Plane Angle, Time, Speed, and Volume.

        ### How to Use:
        1. **Select a Category**: Choose the type of unit you want to convert (e.g., Currency, Distance, etc.).
        2. **Choose Units**: Select the "From" and "To" units.
        3. **Enter Value**: Input the value you want to convert.
        4. **Click Convert**: See the result instantly!

        ### Features:
        - Real-time currency conversion using ExchangeRate-API.
        - Simple and intuitive interface.
        - Supports a wide range of units and categories.

        Made with ❤️ by Muhammad Zakriya.  
        Feel free to reach out for feedback or suggestions!
    """)
    st.markdown("---")
    st.write("🔗 [GitHub Repository](https://github.com/MZakriya/Unit_Converter)")  # GitHub repo link


# Main app
st.title("📏 Unit Converter")
st.markdown("### Convert between different units easily!")

# Category selection
category = st.selectbox(
    "Select Category",
    ["Distance", "Temperature", "Weight", "Pressure", "Area", "Length", "Data Transfer Rate", "Digital Storage", "Energy", "Frequency", "Fuel Economy", "Mass", "Plane Angle", "Time", "Speed", "Volume", "Currency"],
    key="category",
)

# Use columns for better layout
col1, col2 = st.columns(2)

if category == "Currency":
    with col1:
        from_currency = st.selectbox("From", options=["USD", "EUR", "GBP", "INR", "JPY", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD" ,"PKR"], key="from_currency")
    with col2:
        to_currency = st.selectbox("To", options=["USD", "EUR", "GBP", "INR", "JPY", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD" ,"PKR"], key="to_currency")
    value = st.number_input("Enter Value", min_value=0.0, format="%.2f", key="value")

    if st.button("Convert"):
        result = currency_converter(from_currency, to_currency, value)
        if result is not None:
            st.success(f"**{value} {from_currency} = {result:.2f} {to_currency}**")
else:
    with col1:
        from_unit = st.selectbox("From", options=["Meters", "Kilometers", "Feet", "Miles"] if category == "Distance" else
                                ["Celsius", "Fahrenheit"] if category == "Temperature" else
                                ["Kilograms", "Grams", "Pounds", "Ounces"] if category == "Weight" else
                                ["Pascals", "Hectopascals", "Kilopascals", "Bar"] if category == "Pressure" else
                                ["Square Meters", "Square Kilometers", "Square Feet", "Square Miles", "Acres"] if category == "Area" else
                                ["Meters", "Kilometers", "Feet", "Miles", "Inches", "Centimeters", "Millimeters"] if category == "Length" else
                                ["Bits per second", "Kilobits per second", "Megabits per second", "Gigabits per second", "Bytes per second", "Kilobytes per second", "Megabytes per second", "Gigabytes per second"] if category == "Data Transfer Rate" else
                                ["Bits", "Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes"] if category == "Digital Storage" else
                                ["Joules", "Kilojoules", "Calories", "Kilocalories", "Kilowatt-hours"] if category == "Energy" else
                                ["Hertz", "Kilohertz", "Megahertz", "Gigahertz"] if category == "Frequency" else
                                ["Miles per gallon", "Kilometers per liter", "Liters per 100 kilometers"] if category == "Fuel Economy" else
                                ["Kilograms", "Grams", "Pounds", "Ounces", "Metric Tons"] if category == "Mass" else
                                ["Degrees", "Radians", "Gradians"] if category == "Plane Angle" else
                                ["Seconds", "Minutes", "Hours", "Days", "Weeks", "Years"] if category == "Time" else
                                ["Meters per second", "Kilometers per hour", "Miles per hour", "Feet per second", "Knots"] if category == "Speed" else
                                ["Liters", "Milliliters", "Cubic Meters", "Cubic Feet", "Gallons"],
                                key="from_unit")

    with col2:
        to_unit = st.selectbox("To", options=["Meters", "Kilometers", "Feet", "Miles"] if category == "Distance" else
                              ["Celsius", "Fahrenheit"] if category == "Temperature" else
                              ["Kilograms", "Grams", "Pounds", "Ounces"] if category == "Weight" else
                              ["Pascals", "Hectopascals", "Kilopascals", "Bar"] if category == "Pressure" else
                              ["Square Meters", "Square Kilometers", "Square Feet", "Square Miles", "Acres"] if category == "Area" else
                              ["Meters", "Kilometers", "Feet", "Miles", "Inches", "Centimeters", "Millimeters"] if category == "Length" else
                              ["Bits per second", "Kilobits per second", "Megabits per second", "Gigabits per second", "Bytes per second", "Kilobytes per second", "Megabytes per second", "Gigabytes per second"] if category == "Data Transfer Rate" else
                              ["Bits", "Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes"] if category == "Digital Storage" else
                              ["Joules", "Kilojoules", "Calories", "Kilocalories", "Kilowatt-hours"] if category == "Energy" else
                              ["Hertz", "Kilohertz", "Megahertz", "Gigahertz"] if category == "Frequency" else
                              ["Miles per gallon", "Kilometers per liter", "Liters per 100 kilometers"] if category == "Fuel Economy" else
                              ["Kilograms", "Grams", "Pounds", "Ounces", "Metric Tons"] if category == "Mass" else
                              ["Degrees", "Radians", "Gradians"] if category == "Plane Angle" else
                              ["Seconds", "Minutes", "Hours", "Days", "Weeks", "Years"] if category == "Time" else
                              ["Meters per second", "Kilometers per hour", "Miles per hour", "Feet per second", "Knots"] if category == "Speed" else
                              ["Liters", "Milliliters", "Cubic Meters", "Cubic Feet", "Gallons"],
                              key="to_unit")

    value = st.number_input("Enter Value", min_value=0.0, format="%.2f", key="value")

    if st.button("Convert"):
        if category == "Distance":
            result = distance_converter(from_unit, to_unit, value)
        elif category == "Temperature":
            result = temperature_converter(from_unit, to_unit, value)
        elif category == "Weight":
            result = weight_converter(from_unit, to_unit, value)
        elif category == "Pressure":
            result = pressure_converter(from_unit, to_unit, value)
        elif category == "Area":
            result = area_converter(from_unit, to_unit, value)
        elif category == "Length":
            result = length_converter(from_unit, to_unit, value)
        elif category == "Data Transfer Rate":
            result = data_transfer_rate_converter(from_unit, to_unit, value)
        elif category == "Digital Storage":
            result = digital_storage_converter(from_unit, to_unit, value)
        elif category == "Energy":
            result = energy_converter(from_unit, to_unit, value)
        elif category == "Frequency":
            result = frequency_converter(from_unit, to_unit, value)
        elif category == "Fuel Economy":
            result = fuel_economy_converter(from_unit, to_unit, value)
        elif category == "Mass":
            result = mass_converter(from_unit, to_unit, value)
        elif category == "Plane Angle":
            result = plane_angle_converter(from_unit, to_unit, value)
        elif category == "Time":
            result = time_converter(from_unit, to_unit, value)
        elif category == "Speed":
            result = speed_converter(from_unit, to_unit, value)
        elif category == "Volume":
            result = volume_converter(from_unit, to_unit, value)

        st.success(f"**{value} {from_unit} = {result:.2f} {to_unit}**")

# Footer
st.markdown("---")
st.markdown("### 🚀 Enjoy using the Unit Converter!")