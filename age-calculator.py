import streamlit as st
from datetime import datetime

# Function to calculate age
def calculate_age(birthdate_str):
    try:
        birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")
        current_date = datetime.today()  # Use the actual current date
        age = current_date.year - birthdate.year

        # Adjust age if birthday hasn't occurred this year
        if (current_date.month, current_date.day) < (birthdate.month, birthdate.day):
            age -= 1

        if birthdate.year > current_date.year:
            return "❌ Invalid input! Birth year cannot be in the future."

        years_to_100 = 100 - age
        message = f"🎂 You are **{age} years old**.\n"
        if years_to_100 > 0:
            message += f"🎯 You will turn **100** in **{years_to_100} years**."
        else:
            message += "🎉 You have **already turned 100** or more!"
        return message

    except ValueError:
        return "⚠️ **Invalid format!** Please enter your birthdate in **DD/MM/YYYY** format."

# Function to set background color
def set_background():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #e0f7fa;  /* Light Cyan */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background color
set_background()

# Streamlit UI
st.title("🕰 Age Calculator")
st.subheader("Find out your exact age and when you'll turn 100!")

birthdate_str = st.text_input("📅 Enter your birthdate (DD/MM/YYYY):")
if st.button("Calculate Age"):
    result = calculate_age(birthdate_str)
    st.success(result)

# Footer
st.markdown("---")
st.markdown("<h3 style='color: red; text-align: center;'>Made by <b>Awais Gohar Tagar</b> ❤️</h3>", unsafe_allow_html=True)
