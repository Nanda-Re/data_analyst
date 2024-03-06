import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Load data from hourly analysis file
try:
    hourly_data = pd.read_csv("bike_analysis.txt", sep=",", skiprows=2)
    if hourly_data is None:
        raise ValueError("Data is None. Please check the format/content of bike_analysis.txt.")
    
    # Print the loaded data for debugging
    st.write("Hourly Data:")
    st.write(hourly_data)

    if "Days" in hourly_data.columns and "Effective Hours" in hourly_data.columns and "Other Hours" in hourly_data.columns:
        total_days_hour = hourly_data["Days"].iloc[0]
        total_bike_users_effective_hours = hourly_data["Effective Hours"].iloc[0]
        total_bike_users_other_hours = hourly_data["Other Hours"].iloc[0]
        
    else:
        ValueError=False    

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

    if "actual_column_name_1" in daily_data.columns and "actual_column_name_2" in daily_data.columns and "actual_column_name_3" in daily_data.columns:
        total_days_day = daily_data["actual_column_name_1"].iloc[0]
        total_users = daily_data["actual_column_name_2"].iloc[0]
        avg_users_per_day = daily_data["actual_column_name_3"].iloc[0]
        avg_users_weekday = daily_data["actual_column_name_4"].iloc[0]
        avg_users_weekend = daily_data["actual_column_name_5"].iloc[0]
    else:
        ValueError=False
except pd.errors.ParserError as e:
    st.error(f"Error reading analisis_penggunaan.txt: {e}")
    st.stop()
except Exception as e:
    st.error(f"An unexpected error occurred while processing analisis_penggunaan.txt: {e}")
    st.stop()

# Chart for Hourly Data

# Data
days = 731
effective_hours = 1653898
other_hours = 3292679

# Create a bar chart
labels = ['Effective Hours', 'Other Hours']
values = [effective_hours, other_hours]

# Streamlit app
st.title('Hours Distribution Chart')

fig1, ax = plt.subplots()
ax.bar(labels, values, color=['blue', 'orange'])
ax.set_ylabel('Hours')

# Display the chart in the Streamlit app
st.pyplot(fig1)


# Chart for Daily Data
# Data
total_hari = 731
rata_rata_pengguna_per_hari = 4504.35
rata_rata_pengguna_hari_kerja = 15701.44
rata_rata_pengguna_akhir_pekan = 2740.46

# Create a bar chart
labels = [ 'Rata-rata Pengguna per Hari', 'Rata-rata Pengguna pada Hari Kerja', 'Rata-rata Pengguna pada Akhir Pekan']
values = [ rata_rata_pengguna_per_hari, rata_rata_pengguna_hari_kerja, rata_rata_pengguna_akhir_pekan]

fig, ax = plt.subplots()
ax.bar(labels, values, color=['blue', 'orange', 'green', 'red'])
ax.set_title('Statistik Pengguna')
ax.set_ylabel('Jumlah Pengguna')

# Display the chart in Streamlit
st.pyplot(fig)



