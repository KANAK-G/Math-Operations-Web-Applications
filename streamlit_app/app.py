import streamlit as st

# Title of the app
st.title("Math Operations App")

# Create input fields for two numbers using text input
num1_input = st.text_input("Enter first number", value="0")
num2_input = st.text_input("Enter second number", value="0")

# Try to convert input to numbers and handle possible errors
try:
    num1 = float(num1_input)
    num2 = float(num2_input)
    valid_input = True
except ValueError:
    valid_input = False
    st.error("Please enter valid numbers")

# Create a dropdown for selecting the operation
operation = st.selectbox("Choose an operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform the operation when the button is clicked
if st.button("Calculate") and valid_input:
    if operation == "Add":
        result = num1 + num2
        st.success(f"The sum of {num1} and {num2} is {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"The difference between {num1} and {num2} is {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"The product of {num1} and {num2} is {result}")
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.success(f"The quotient when {num1} is divided by {num2} is {result}")
        else:
            st.error("Division by zero is not allowed")
