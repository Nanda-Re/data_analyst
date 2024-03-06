import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Load data from hourly analysis file
try:
    hourly_data = pd.read_csv("bike_analysis.txt", sep=",", skiprows=2)
    if hourly_data is None:
        raise ValueError("Data is None. Please check the format/content of bike_analysis.txt.")

    # Extract relevant information
    if "Days" in hourly_data.columns:
        total_days_hour = hourly_data["Days"].iloc[0]
    else:
        total_days_hour = 0

except pd.errors.ParserError as e:
    st.error(f"Error reading bike_analysis.txt: {e}")
    st.stop()
except Exception as e:
    st.error(f"An unexpected error occurred while processing bike_analysis.txt: {e}")
    st.stop()

# Load data from daily analysis file
try:
    daily_data = pd.read_csv("analisis_penggunaan.txt", sep=",", skiprows=1)
    if daily_data is None:
        raise ValueError("Data is None. Please check the format/content of analisis_penggunaan.txt.")

    # Extract relevant information
    if "actual_column_name_1" in daily_data.columns:
        total_days_day = daily_data["actual_column_name_1"].iloc[0]
    else:
        total_days_day = 0

except pd.errors.ParserError as e:
    st.error(f"Error reading analisis_penggunaan.txt: {e}")
    st.stop()
except Exception as e:
    st.error(f"An unexpected error occurred while processing analisis_penggunaan.txt: {e}")
    st.stop()

# Bar chart
fig, ax = plt.subplots()

# Data for the bar chart
labels = ['Hourly Analysis', 'Daily Analysis']
values = [total_days_hour, total_days_day]

# Plotting the bar chart
ax.bar(labels, values)

# Adding labels and title
ax.set_ylabel('Total Days')
ax.set_title('Total Days for Hourly and Daily Analysis')

# Show the chart using Streamlit
st.pyplot(fig)
