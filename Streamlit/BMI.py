
import streamlit as st

# App title
st.title("🏥 BMI Calculator")
st.write("Calculate your Body Mass Index (BMI)")

# User inputs
weight = st.number_input(
    "Enter your weight (kg)",
    min_value=1.0,
    max_value=300.0,
    value=60.0
)

height = st.number_input(
    "Enter your height (cm)",
    min_value=50.0,
    max_value=250.0,
    value=170.0
)

# Calculate BMI
if st.button("Calculate BMI"):

    height_m = height / 100

    bmi = weight / (height_m ** 2)

    st.subheader("Your BMI Result")

    st.metric("Your BMI", f"{bmi:.2f}")

    # BMI category
    if bmi < 18.5:
        st.warning("Underweight")
    elif bmi < 25:
        st.success("Normal weight")
    elif bmi < 30:
        st.warning("Overweight")
    else:
        st.error("Obesity")

    st.info("BMI is a screening measure, not a diagnosis.")
