import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Load data from hourly analysis file
try:
    hourly_data = pd.read_csv("bike_analysis.txt", sep=",", skiprows=2, error_bad_lines=False)
    if hourly_data is None:
        raise ValueError("Data is None. Please check the format/content of bike_analysis.txt.")
    
    # Print the loaded data for debugging
    st.write("Hourly Data:")
    st.write(hourly_data)

    total_days_hour = hourly_data["Days"].iloc[0]
    total_bike_users_effective_hours = hourly_data["Effective Hours"].iloc[0]
    total_bike_users_other_hours = hourly_data["Other Hours"].iloc[0]

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
    
    # Print the loaded data for debugging
    st.write("Daily Data:")
    st.write(daily_data)

    total_days_day = daily_data["Total Hari"].iloc[0]
    total_users = daily_data["Total Pengguna"].iloc[0]
    avg_users_per_day = daily_data["Rata-rata Pengguna per Hari"].iloc[0]
    avg_users_weekday = daily_data["Rata-rata Pengguna pada Hari Kerja"].iloc[0]
    avg_users_weekend = daily_data["Rata-rata Pengguna pada Akhir Pekan"].iloc[0]

except pd.errors.ParserError as e:
    st.error(f"Error reading analisis_penggunaan.txt: {e}")
    st.stop()
except Exception as e:
    st.error(f"An unexpected error occurred while processing analisis_penggunaan.txt: {e}")
    st.stop()

# Rest of the code remains unchanged...
