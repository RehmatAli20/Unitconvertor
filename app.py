import streamlit as st

st.title("Unit Converter 🔄")
st.sidebar.header("Select Conversion Type")
conversion_type = st.sidebar.selectbox(
    "Choose a conversion type:",
    ["Length", "Weight", "Temperature"]
)

def convert_length(value, from_unit, to_unit):
    length_factors = {
        "Millimeter": 0.001,
        "Centimeter": 0.01,
        "Meter": 1.0,
        "Kilometer": 1000.0,
        "Inch": 0.0254,
        "Foot": 0.3048,
        "Yard": 0.9144,
        "Mile": 1609.34
    }

    meters = value * length_factors[from_unit]

    result = meters / length_factors[to_unit]
    return result

def convert_weight(value, from_unit, to_unit):
    
    weight_factors = {
        "Milligram": 0.001,
        "Gram": 1.0,
        "Kilogram": 1000.0,
        "Tonne": 1000000.0,
        "Ounce": 28.3495,
        "Pound": 453.592,
        "Stone": 6350.29
    }
    
    grams = value * weight_factors[from_unit]
    
    result = grams / weight_factors[to_unit]
    return result

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
        else:
            return value
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        else:
            return value
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value

# Main app logic
if conversion_type == "Length":
    st.header("Length Converter")
    col1, col2 = st.columns(2)
    with col1:
        length_value = st.number_input("Enter length value:", min_value=0.0)
        from_length_unit = st.selectbox(
            "From unit:",
            ["Millimeter", "Centimeter", "Meter", "Kilometer", "Inch", "Foot", "Yard", "Mile"]
        )
    with col2:
        to_length_unit = st.selectbox(
            "To unit:",
            ["Millimeter", "Centimeter", "Meter", "Kilometer", "Inch", "Foot", "Yard", "Mile"]
        )
    if st.button("Convert Length"):
        result = convert_length(length_value, from_length_unit, to_length_unit)
        st.success(f"✅ {length_value} {from_length_unit} = {result:.4f} {to_length_unit}")

elif conversion_type == "Weight":
    st.header("Weight Converter")
    col1, col2 = st.columns(2)
    with col1:
        weight_value = st.number_input("Enter weight value:", min_value=0.0)
        from_weight_unit = st.selectbox(
            "From unit:",
            ["Milligram", "Gram", "Kilogram", "Tonne", "Ounce", "Pound", "Stone"]
        )
    with col2:
        to_weight_unit = st.selectbox(
            "To unit:",
            ["Milligram", "Gram", "Kilogram", "Tonne", "Ounce", "Pound", "Stone"]
        )
    if st.button("Convert Weight"):
        result = convert_weight(weight_value, from_weight_unit, to_weight_unit)
        st.success(f"✅ {weight_value} {from_weight_unit} = {result:.4f} {to_weight_unit}")

elif conversion_type == "Temperature":
    st.header("Temperature Converter")
    col1, col2 = st.columns(2)
    with col1:
        temp_value = st.number_input("Enter temperature value:")
        from_temp_unit = st.selectbox(
            "From unit:",
            ["Celsius", "Fahrenheit", "Kelvin"]
        )
    with col2:
        to_temp_unit = st.selectbox(
            "To unit:",
            ["Celsius", "Fahrenheit", "Kelvin"]
        )
    if st.button("Convert Temperature"):
        result = convert_temperature(temp_value, from_temp_unit, to_temp_unit)
        st.success(f"✅ {temp_value} {from_temp_unit} = {result:.4f} {to_temp_unit}")

