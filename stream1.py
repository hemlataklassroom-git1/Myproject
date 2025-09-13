import streamlit as st

st.title("My First Streamlit App 🎉")

# Text Input
name = st.text_input("Enter your name")
st.write("Hello", name)

# Number Input
num = st.number_input("Enter a number", min_value=0, max_value=100)
st.write("Squared:", num ** 2)

# Slider
value = st.slider("Select a value", 0, 10)
st.write("You selected:", value)

# Button
if st.button("Click me"):
    st.write("Button clicked!")
