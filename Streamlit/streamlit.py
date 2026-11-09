import streamlit as st

st.title("This is my first streamlit application")
st.write("Hello! Welcome to Streamlit.")

name = st.text_input("Enter your name:")
st.write("Hello,", name)

age = st.number_input("Enter your age:")
st.write("Your age is", age)

if st.button("Click Me"):
    st.write("You clicked the button! 🎉")

number = st.slider("Pick a number", 0, 100)
st.write("You picked:", number)